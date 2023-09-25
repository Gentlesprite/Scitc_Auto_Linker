# coding=UTF-8
# Author:LZY/我不是盘神
# Software:PyCharm
# Time:2023/4/1 20:43:42
# File:resq.py
import socket


class Url:
    @staticmethod
    def url_login():
        url_login = 'http://10.10.11.14/portal.do?wlanuserip=' + \
                    Get_ip.get_host_ip() + '&wlanacname=XF_BRAS'
        return url_login

    @staticmethod
    def url_logout():
        url_logout = 'http://10.10.11.14/webdisconn.do?wlanuserip=' + \
                     Get_ip.get_host_ip() + '&wlanacname=XF_BRAS'
        return url_logout


class Headers:
    @staticmethod
    def headers_pc():
        headers_pc = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.9999.0 Safari/537.36"}
        return headers_pc

    @staticmethod
    def headers_phone():
        headers_phone = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 12; CPH2199) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36"}
        return headers_phone


class Get_ip:
    @staticmethod
    def get_host_ip():
        global get_host_way
        try:
            get_host_way = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            get_host_way.connect(('8.8.8.8', 80))
            host_ip = get_host_way.getsockname()[0]
        finally:
            get_host_way.close()
        return host_ip

    @staticmethod
    def get_local_ip():
        local_ip = socket.gethostbyname(socket.gethostname())
        return local_ip