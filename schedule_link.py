# coding=UTF-8
# Author:LZY/我不是盘神
# Software:PyCharm
# Time:2023/4/1 23:45:49
# File:schedule_link.py
import requests
import socket
import pywifi
import threading
import time

import urllib.request

# def is_internet_available():
#     try:
#         urllib.request.urlopen('http://baidu.com', timeout=1)
#         return True
#     except urllib.error.URLError:
#         pass
#     return False

KEYWORD = "ChinaNet"
MAX_CONNECT_TRY = 3


class WifiScanner:
    def __init__(self):
        self.wifi = pywifi.PyWiFi()
        self.interface = self.wifi.interfaces()[0]
        self.result = []
        self.lock = threading.Lock()

    def scan(self):
        self.interface.scan()
        result = self.interface.scan_results()
        with self.lock:
            self.result = result

    def filter(self):
        filtered_result = []
        for wifi in self.result:
            if KEYWORD in wifi.ssid and wifi.signal > -80 and wifi.akm[0] == pywifi.const.AUTH_ALG_OPEN:
                filtered_result.append(wifi)
        return filtered_result

    def connect(self, wifi):
        profile = pywifi.Profile()
        profile.ssid = wifi.ssid
        profile.auth = pywifi.const.AUTH_ALG_OPEN
        profile.akm.append(pywifi.const.AKM_TYPE_NONE)

        self.interface.disconnect()
        # self.interface.remove_all_network_profiles() #一但匹配连接成功,该代码会清除所有以前已经连接过的所有记录
        tmp_profile = self.interface.add_network_profile(profile)

        for i in range(MAX_CONNECT_TRY):
            if self.interface.status() in [pywifi.const.IFACE_DISCONNECTED, pywifi.const.IFACE_INACTIVE]:
                self.interface.connect(tmp_profile)
                if self.interface.status() == pywifi.const.IFACE_CONNECTED:
                    print(f"Connected to {wifi.ssid} with signal strength {wifi.signal}")
                    break
            elif self.interface.status() == pywifi.const.IFACE_CONNECTED:
                break


class WifiConnector:
    def __init__(self):
        self.scanner = WifiScanner()

    def run(self):
        global ssid
        threads = []
        for i in range(10):
            t = threading.Thread(target=self.scanner.scan)
            threads.append(t)
            t.start()
        for t in threads:
            t.join()
        filtered_results = self.scanner.filter()
        for result in filtered_results:
            ssid = result.ssid
        if len(filtered_results) == 1:
            self.scanner.connect(filtered_results[0])
            print(f"Scan only one signal:{ssid}")
            return True
        elif len(filtered_results) >= 2:
            print(f"Scan multiple signal,the best is:{ssid}")
            sorted_results = sorted(filtered_results, key=lambda x: x.signal, reverse=True)
            self.scanner.connect(sorted_results[0])
            return True
        else:
            print("Non campus network, connect school network failed.")
            return False

def main():
    def get_host_ip():
        global s
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(('8.8.8.8', 80))
            ip = s.getsockname()[0]
        finally:
            s.close()
        return ip

    url = 'http://10.10.11.14/portal.do?wlanuserip=' + get_host_ip() + '&wlanacname=XF_BRAS'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 12; CPH2199) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36'}
    data = {'auth_type': '0', 'isBindMac1': '0', 'pageid': '1', 'templatetype': '3', 'listbindmac': '0',
            'recordmac': '0', 'isRemind': '0', 'userId': 'XYGY_S账号@SCITC', 'passwd': '密码'}

    resp = requests.post(url=url, data=data, headers=headers).status_code
    if resp == 200:
        print('Success!')
    else:
        print('Failure!')


def connect_school_network() -> int:
    global failure_info
    start_time = time.time()
    connector = WifiConnector()
    success = connector.run()
    end_time = time.time()
    takes_time = int(end_time - start_time)
    if success:
        time.sleep(2)  # wait 1s to connect
        print(f'connecting {ssid}...')
        print(f'Successfully!It takes {takes_time}s, have fun!')
        main()
        return takes_time
    else:
        # print("Connect school network failed.")
        return -1  # 连接失败返回-1或其他错误码


if __name__ == "__main__":
    # if is_internet_available():
    #     print("Internet is available, exit program.")
    # else:
    connect_school_network()
    main()
