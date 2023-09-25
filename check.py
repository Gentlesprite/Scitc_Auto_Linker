# codidng=utf-8
# Author:LZY/我不是盘神
# Software:PyCharm
# Time:2023/3/5 20:39:40
# File:check.py
import os, sys
from MyPing import *
import threading
import pywifi
import time


# class CustomTask:
#
#     def __init__(self):
#         self._result = None
#
#     def run(self, *args, **kwargs):
#         # 你的代码, 你用来进行多线程
#         result = net_env_det('127.0.0.1')
#
#         self._result = result
#
#
#     def get_result(self):
#         return self._result

def check_soft_env():
    # 获取exe的路径并写入当前目录
    global application_path
    if hasattr(sys, 'frozen'):  # 判断为运行打包好exe软件
        application_path = os.path.dirname(sys.executable)
    elif __file__:  # 判断为代码运行软件
        application_path = os.path.dirname(os.path.abspath(__file__))
    return application_path


def ping(host: str):  # 网络环境检测

    # host = "10.10.11.14"
    host = host
    # host = '172.20.10.1' #test host
    ping = MyPing()
    sumtime, shorttime, longtime, avgtime = 0, 1000, 0, 0
    # 8回射请求 11超时 0回射应答
    data_type = 8
    data_code = 0
    # 检验和
    data_checksum = 0
    # ID
    data_ID = 0
    # 序号
    data_Sequence = 1
    # 可选的内容
    payload_body = b'scitc scheduled linker by lzy'
    dst_addr = socket.gethostbyname(host)
    print("正在 Ping {0} [{1}] 具有 32 字节的数据:".format(host, dst_addr))
    # 发送3次

    for i in range(0, 3):
        # 请求ping数据包的二进制转换
        icmp_packet = ping.request_ping(data_type, data_code, data_checksum, data_ID, data_Sequence + i,
                                        payload_body)
        # 连接套接字,并将数据发送到套接字
        send_request_ping_time, rawsocket = ping.raw_socket(dst_addr, icmp_packet)
        # 数据包传输时间
        times = ping.reply_ping(send_request_ping_time, rawsocket, data_Sequence + i)
        if times > 0:
            print("来自 {0} 的回复: 字节=32 时间={1}ms".format(dst_addr, int(times * 1000)))
            return_time = int(times * 1000)
            sumtime += return_time
            if return_time > longtime:
                longtime = return_time
            if return_time < shorttime:
                shorttime = return_time
            time.sleep(1.4)
            return True
        else:
            return False


# 定义需要搜索的关键字
KEYWORD = "ChinaNet"

# 定义连接wifi的最大尝试次数
MAX_CONNECT_TRY = 3


# 定义了一个WIFI扫描器，用于扫描当前可用的WIFI信号。
# 使用pywifi库进行wifi扫描和连接。WifiScanner类中的scan方法用于扫描可用的WIFI信号
# filter方法用于过滤出符合条件的WIFI信号，过滤wifi信息，返回符合特定条件的wifi信息列表。其中，filtered_result为符合条件的wifi信息列表，KEYWORD为关键字，wifi.ssid为wifi名称，wifi.signal为信号强度，wifi.akm[0]为认证算法。
# connect方法用于连接指定的WIFI信号。

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
        filtered_result = []  # 定义一个空列表，用于存储符合条件的wifi信息
        for wifi in self.result:  # 遍历self.result中的每一个wifi信息
            # 判断该wifi的ssid是否包含关键字，并且信号强度大于-80，认证算法为开放式
            if KEYWORD in wifi.ssid and wifi.signal > -80 and wifi.akm[0] == pywifi.const.AUTH_ALG_OPEN:
                filtered_result.append(wifi)  # 如果符合条件，将该wifi信息添加到filtered_result列表中
        return filtered_result  # 返回符合条件的wifi信息列表

    def connect(self, wifi):
        profile = pywifi.Profile()
        profile.ssid = wifi.ssid
        profile.auth = pywifi.const.AUTH_ALG_OPEN
        profile.akm.append(pywifi.const.AKM_TYPE_NONE)

        self.interface.disconnect()
        self.interface.remove_all_network_profiles()
        tmp_profile = self.interface.add_network_profile(profile)

        for i in range(MAX_CONNECT_TRY):  # 尝试连接KEYWORD中指定的WiFi网络
            # 无线网络的状态是否为断开连接或未激活状态
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
            print(f"只有一个信号:{ssid}")
            return True
        elif len(filtered_results) >= 2:
            print(f"网络环境有多个信号,筛选信号最好的结果是:{ssid}")
            sorted_results = sorted(filtered_results, key=lambda x: x.signal, reverse=True)
            self.scanner.connect(sorted_results[0])
            return True
        else:
            print("环境非校园网")
            return False


def check_school_env():
    connector = WifiConnector()
    return connector.run()


def connect_school_network() -> int:
    start_time = time.time()
    connector = WifiConnector()
    connector.run()
    time.sleep(2)  # 延迟1秒等待wifi连接
    end_time = time.time()
    takes_time = int(end_time - start_time)
    print(f'连接校园网共耗时{takes_time}秒')
    return takes_time


def network_connection(host: str):  # 判断是否可以上网
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((host, 80))
        return True
    except:
        return False
    finally:
        sock.close()


# def school_network():
#     global t
#     ct = CustomTask()
#     t = threading.Thread(target=ct.run)
#     t.start()
#
#     # thread_school = threading.Thread(target=ct.run)
#     result = ct.get_result()
#     return result
