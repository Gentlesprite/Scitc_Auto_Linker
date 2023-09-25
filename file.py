# coding=utf-8
# Author:LZY/我不是盘神
# Software:PyCharm
# Time:2023/3/15 19:12:10
# File:file.py
from check import *


class Dir_File:
    @staticmethod
    def start_up_dir():
        start_up_dir = 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\StartUp\\'
        # 目录:C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp\
        return start_up_dir


class Make_File:

    @staticmethod
    def make_bat_startup():  # 在starup目录下创建bat文件
        with open(file=Dir_File.start_up_dir() + 'schedule_link.bat',
                  mode='w') as bat_startup:
            bat_startup.write(check_soft_env() + '\\venv\\python.exe ' + check_soft_env() + '\\schedule_link.py')
            # bat_startup.write(check_soft_env() + '\\venv\\python.exe schedule_link.py')

    @staticmethod
    def make_bat_local():  # 在软件目录下创建bat文件
        with open(file='schedule_link.bat',
                  mode='w') as bat_local:
            bat_local.write('%~dp0\\venv\\python.exe ' + '%~dp0' + 'schedule_link.py')


def code(headers, data):
    codes = '''
# coding=UTF-8
# Author:LZY
# Software:PyCharm
import requests
import socket
import pywifi
import threading
import time
def is_internet_available():
    try:
        socket.create_connection(('www.baidu.com', 80))  # 连接百度服务器的 80 端口
        return True
    except OSError:
        pass
    return False
    
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
            print(f"only one signal{ssid}")
            return True
        elif len(filtered_results) >= 2:
            print(f"one more signal{ssid}")
            sorted_results = sorted(filtered_results, key=lambda x: x.signal, reverse=True)
            self.scanner.connect(sorted_results[0])
            return True
        else:
            print("Non campus network")
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
'''
    codes += f'''
    headers = {headers}
    data = {data}
'''
    codes + '''
    data = {"loginType": "",
            "auth_type": "0",
            "isBindMac1": "0",
            "pageid": "1",
            "templatetype": "3",
            "listbindmac": "0",
            "recordmac": "0",
            "isRemind": "0",
            "loginTimes": "",
            "groupId": "",
            "distoken": "",
            "echostr": "",
            "url": "",
            "isautoauth": "",
            "notice_pic_loop2": "/portal/uploads/general/demo1/image/banner.jpg",
            "userId": '{acc}',  # account
            "passwd": '{pwd}',  # password
            }
'''
    codes += '''
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
    if is_internet_available():
        print("Internet is available, exit program.")
    else:
        connect_school_network()
        main()

'''
    return codes
