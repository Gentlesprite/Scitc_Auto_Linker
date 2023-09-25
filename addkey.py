# coding=utf-8
# Author:LZY/我不是盘神
# Software:PyCharm
# Time:2023/3/19 15:49:40
# File:addkey.py

import random, string, base64


# 将内容转为base64格式内容
def encode_base64(code):
    try:
        tmpBytes = code.encode()
        tmpBase64 = base64.b64encode(tmpBytes)
        return tmpBase64
    except Exception as e:
        print('异常：', e)


# 将base64格式内容转为正常信息
def decode_base64(*code):
    try:
        tmpBytes = base64.b64decode(*code)
        tmpStr = tmpBytes.decode()
        return tmpStr
    except Exception as e:
        print('异常：', e)


'''
print(bytes.decode(encode_base64('python')))
print(decode_base64(encode_base64('python')))

#读取config.ini文件
file = open(r"D:\study\Python\Program\scitc_auto_link\version\1.0.4\config.ini", "r", encoding="utf-8")
data = str(encode_base64(file.read()))#读取内容并且加密
file.close()#结束进程

#将加密后的写入config.ini
with open(r"D:\study\Python\Program\scitc_auto_link\version\1.0.4\config.ini",mode="r+",encoding="utf-8") as f:
    f.write(data)
'''


def create_random(count):  # 生成字幕随机数传一个数字代表生成密码的个数

    src = string.ascii_letters + string.digits
    list_passwds = []
    for i in range(count):
        list_passwd_all = random.sample(src, 5)  # 从字母和数字中随机取5位
        list_passwd_all.extend(random.sample(string.digits, 1))  # 让密码中一定包含数字
        list_passwd_all.extend(random.sample(string.ascii_lowercase, 1))  # 让密码中一定包含小写字母
        list_passwd_all.extend(random.sample(string.ascii_uppercase, 1))  # 让密码中一定包含大写字母
        random.shuffle(list_passwd_all)  # 打乱列表顺序
        str_passwd = ''.join(list_passwd_all)  # 将列表转化为字符串
        if str_passwd not in list_passwds:  # 判断是否生成重复密码
            list_passwds.append(str_passwd)

    return str(list_passwds)
