# coding=utf-8
# Author:LZY/我不是盘神
# Software:PyCharm
# Time:2023/3/22 17:29:39
# File:info.py
import webbrowser
from main import *
import time

class Author_info:
    @staticmethod
    def add_qq():
        qq = 2286502367
        webbrowser.open(
            f"tencent://AddContact/?fromId=45&fromSubId=1&subcmd=all&uin={qq}&website=www.oicqzone.com")

    @staticmethod
    def add_douyin():
        douyin = 'https://www.iesdouyin.com/share/user/MS4wLjABAAAA2x9EiFK719Hn3lQqggUu35Gvy7hbFDYDKifJy6OzYPE?iid=MS4wLjABAAAA1O9sInvU8fCRrDCuJMXx3UvPitAPkVqD3H2Pzp5jjmQ&with_sec_did=1&sec_uid=MS4wLjABAAAA2x9EiFK719Hn3lQqggUu35Gvy7hbFDYDKifJy6OzYPE&from_ssr=1&u_code=jgfebk10&did=MS4wLjABAAAARFYYJbsG_SwY_fyDphMYCsPxg-UFAgEkGO0ywwqFM1btvEB7lsTEkyW74DIgyFTT&utm_campaign=client_share&app=aweme&utm_medium=ios&tt_from=copy&utm_source=copy'
        webbrowser.open(douyin)

    @staticmethod
    def add_bilibili():
        bilibili = 'https://space.bilibili.com/305337179?spm_id_from=333.1007.0.0'
        webbrowser.open(bilibili)

    @staticmethod
    def add_kuaishou():
        kuaishou = 'https://www.kuaishou.com/profile/3xd8ghypfn8tzm2'
        webbrowser.open(kuaishou)

    @staticmethod
    def author_email():
        email = b'gentlesprites@gmail.com'
        return str(bytes.decode(email))

    @staticmethod
    def author_name():
        name = b'Gentlesprites'
        return str(bytes.decode(name))
class Time:
    @staticmethod
    def now():
        return time.strftime('%Y{y}%m{m}%d{d}%H{h}%M{f}%S{s}').format(y='年', m='月', d='日', h='时', f='分', s='秒')

    @staticmethod
    def hour():
        get_hour = time.strftime('%H')
        return int(get_hour)



