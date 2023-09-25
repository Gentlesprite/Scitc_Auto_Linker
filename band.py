# coding=UTF-8
# Author:LZY/我不是盘神
# Software:PyCharm
# Time:2023/3/12 12:09:12
# File:band.py

from main import MainWindow


class Band(MainWindow):
    def __init__(self):
        super(Band, self).__init__()

    def clogin_ui(self):
        self.ui.money_ui.hide()
        self.ui.clogin_ui.show()
        self.ui.cabout_ui.show()

    def cabout_ui(self):
        self.ui.clogin_ui.hide()
        self.ui.cabout_ui.hide()
        self.ui.money_ui.show()

    def money_ui(self):
        self.ui.clogin_ui.hide()
        self.ui.cabout_ui.hide()
        self.ui.pushButton_douyin.hide()
        self.ui.pushButton_bilibili.hide()
        self.ui.pushButton_qq.hide()
        self.ui.pushButton_kuaishou.hide()
        self.ui.pushButton_tips.hide()
        self.ui.pushButton_author.hide()
        self.ui.img_pay.show()
        self.ui.pushButton_quit_pay.show()
        self.ui.pushButton_quit.hide()
        self.ui.pushButton_mini.hide()
