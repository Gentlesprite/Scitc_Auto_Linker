# coding=utf-8
# Author:LZY/我不是盘神
# Software:PyCharm
# Time:2023/3/24 23:01:40
# File:admin.py
import ctypes


def is_admin():  # 判断当前是否为管理员
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        # ctypes.windll.shell32.ShellExecuteW(None, 'runas', sys.executable, __file__, None, 1) # 自动重启获得管理员
        return False

# print(bool(is_admin()))
