# encoding='utf-8'
# Author:LZY/我不是盘神
# Software:PyCharm
# Time:2023/3/16 15:08:13
# File:re_get.py
import re


def find_md5(params):  # 传html内容分拣出32位md5值
    pattern = re.compile(r'[a-f\d]{32}')
    # return pattern.search(params)  返回位置+结果
    # str_md5 = str(pattern.findall(params))
    return pattern.findall(params)


'''
# 实例
a = "<input id=distASDASDASDASDADoken name=distoASDASvalue=390e2633f1c9f65bca9bc9f8b3d16777"
print(find_md5(a))
'''

def find_stu_num(params):
    pattern = re.search(r'\d+', params).group()
    return pattern
