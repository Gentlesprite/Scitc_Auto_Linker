# coding=utf-8
# Author:LZY/我不是盘神
# Software:PyCharm
# Time:2023/3/1 23:25:44
# File:main.py
import threading
import time
from threading import Thread

'''
参考:
多线程https://blog.csdn.net/qq_23390957/article/details/122690146
'''
import PySide2.QtCore
from PySide2 import QtWidgets
from info import *
from resq import *
from file import *
from admin import *
from addkey import *
from re_get import *
from bs4 import BeautifulSoup
from ui import *
import requests
from win10toast import ToastNotifier


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.band()
        self.textBrowser = QTextBrowser()
        self.setAcceptDrops(True)
        self.setWindowFlags(Qt.FramelessWindowHint)  # 隐藏状态栏
        self.setAttribute(Qt.WA_TranslucentBackground)  # 背景透明
        self.clogin_ui()  # 默认切换为首页1
        self.ui.img_pay.hide()  # 隐藏支付界面
        self.ui.pushButton_quit_pay.hide()  # 隐藏支付关闭按钮
        self.ui.pushButton_logout_pc.hide()  # 隐藏电脑注销按钮
        self.ui.pushButton_logout_phone.hide()  # 隐藏手机注销按钮
        self.ui.pushButton_schedule_link_exh.setEnabled(False)  # 锁定自动登录展示按钮
        self.ui.pushButton_logout_exh.setEnabled(True)  # 锁定注销登录展示按钮
        self.ui.pushButton_schedule_link_pc.setEnabled(False)  # 锁定自动登录按钮
        self.ui.pushButton_schedule_link_phone.setEnabled(False)  # 锁定自动登录按钮
        self.ui.pushButton_schedule_link_cancel.setEnabled(False)  # 打开取消自动登录按钮
        self.ui.pushButton_logout_pc.setEnabled(False)  # 锁定电脑身份注销按钮
        self.ui.pushButton_logout_phone.setEnabled(False)  # 锁定手机身份注销按钮
        self.settings = QSettings("config.ini", QSettings.IniFormat)
        self.init_login_info()  # 显示上一次输入所保存的账号和密码
        self.ui.lineEdit_acc.setValidator(
            QRegExpValidator(QRegExp("[^\u4e00-\u9fa5\s]{25}")))  # 用正则表达式实现禁止输入中文和空白字符，限制25位
        self.ui.lineEdit_pwd.setValidator(
            QRegExpValidator(QRegExp("[^\u4e00-\u9fa5\s]{35}")))  # 用正则表达式实现禁止输入中文和空白字符，限制25位
        self.tn = ToastNotifier()

    def band(self):
        self.ui.pushButton_clogin.clicked.connect(self.clogin_ui)  # 主界面的‘登录’字体点了以后就会切换为主界面
        self.ui.pushButton_back.clicked.connect(self.clogin_ui)  # 这是在点进关于作者界面了以后设置一个返回按钮来返回到主界面
        self.ui.pushButton_cabout.clicked.connect(self.cabout_ui)  # 点击主界面顶部‘关于作者’了以后，切换到关于作者页面
        self.ui.pushButton_money.clicked.connect(self.money_ui)  # 这是在‘关于作者’页面，捐赠作者按钮点击后弹出作者支付宝，微信收款码
        self.ui.pushButton_login_pc.clicked.connect(self.advance_check_pc)  # 主功能,输入账号密码后的登录按钮，注意这里构造以电脑身份登录
        self.ui.pushButton_login_phone.clicked.connect(
            self.advance_check_phone)  # 主功能,输入账号密码后的登录按钮，注意这里构造以手机身份登录
        self.ui.pushButton_logout_pc.clicked.connect(self.logout_pc)  # 注销电脑身份的登录
        self.ui.pushButton_logout_phone.clicked.connect(self.logout_phone)  # 注销手机身份的登录

        self.ui.pushButton_logout_exh.clicked.connect(self.logout_exh)

        self.ui.pushButton_mini.clicked.connect(self.mini)  # 点击使软件最小化
        self.ui.pushButton_quit.clicked.connect(self.quit)  # 点击使软件关闭
        self.ui.pushButton_quit_pay.clicked.connect(self.quit2)  # 关闭‘关于作者’界面捐赠作者的收款码的按钮
        self.ui.pushButton_schedule_link_pc.clicked.connect(self.schedule_link_pc)  # 特色功能:构造电脑身份开机自动登录功能
        self.ui.pushButton_schedule_link_phone.clicked.connect(
            self.schedule_link_phone)  # 特色功能:构造手机身份开机自动登录功能
        self.ui.pushButton_schedule_link_cancel.clicked.connect(
            self.schedule_link_cancel)  # 取消自动登录:代码已实现自动检测是手机还是电脑身份构造的开机自动登录,所以只为一个
        self.ui.pushButton_schedule_link_force_cancel.clicked.connect(self.schedule_link_force_cancel)
        self.ui.pushButton_qq.clicked.connect(Author_info.add_qq)
        self.ui.pushButton_douyin.clicked.connect(Author_info.add_douyin)
        self.ui.pushButton_bilibili.clicked.connect(Author_info.add_bilibili)
        self.ui.pushButton_kuaishou.clicked.connect(Author_info.add_kuaishou)
        self.ui.checkBox_rem.clicked.connect(self.remember)  # 勾选框的记住密码
        self.ui.checkBox_show_pwd.clicked.connect(self.show_pwd)  # 勾选框的显示密码

    def quit(self):
        self.ui.checkBox_rem.clicked.connect(self.remember)
        self.close()
        sys.exit()

    def quit2(self):
        self.ui.img_pay.hide()
        self.ui.pushButton_quit_pay.hide()
        self.ui.pushButton_douyin.show()
        self.ui.pushButton_bilibili.show()
        self.ui.pushButton_qq.show()
        self.ui.pushButton_kuaishou.show()
        self.ui.pushButton_tips.show()
        self.ui.pushButton_author.show()
        self.ui.pushButton_quit.show()
        self.ui.pushButton_mini.show()

    def mini(self):
        self.showMinimized()

    # 重写鼠标事件
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))

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

    def hello(self):  # 把学校的问候语原封不动扒了过来
        hour = Time().hour()
        if hour < 6:
            return u'凌晨好, '
        elif hour < 9:
            return u'早上好, '
        elif hour < 12:
            return u'上午好, '
        elif hour < 14:
            return u'中午好, '
        elif hour < 17:
            return u'下午好,'
        elif hour < 19:
            return u'傍晚好, '
        else:
            return u'夜深了, 请注意休息！'

    def data_logio(self, io: str):
        if io == 'in':
            data_login = {"auth_type": "0",
                          "isBindMac1": "0",
                          "pageid": "1",
                          "templatetype": "3",
                          "listbindmac": "0",
                          "recordmac": "0",
                          "isRemind": "0",
                          "userId": f"{self.userinfo('acc')}",
                          "passwd": f"{self.userinfo('pwd')}", }
            return data_login
        elif io == 'out':
            acc = self.userinfo('acc')
            data_logout = {'loginType': '',
                           'auth_type': '0',
                           'isBindMac1': '1',
                           'pageid': '1',
                           'templatetype': '1',
                           'listbindmac': '1',
                           'recordmac': '0',
                           'isRemind': '1',
                           'distoken': f'{self.distoken()}',
                           'url': "http://1.1.1.1",
                           'userId': f'{acc}',
                           'other1': 'disconn', }
            return data_logout
        elif io == 'out_normal':
            acc = self.userinfo('acc')
            distoken = self.settings.value('distoken')
            data_logout = {'loginType': '',
                           'auth_type': '0',
                           'isBindMac1': '1',
                           'pageid': '1',
                           'templatetype': '1',
                           'listbindmac': '1',
                           'recordmac': '0',
                           'isRemind': '1',
                           'distoken': f'{distoken}',
                           'url': "http://1.1.1.1",
                           'userId': f'{acc}',
                           'other1': 'disconn', }
            return data_logout

    def resp_logio(self, headers, io: str):
        if io == 'in':  # 登录操作
            resp_login = requests.post(url=Url.url_login(), data=self.data_logio('in'), headers=headers)
            return resp_login
        elif io == 'out':  # 注销操作
            resp_logout = requests.post(url=Url.url_logout(), data=self.data_logio('out'), headers=headers)
            return resp_logout
        elif io == 'out_normal':  # 正常注销
            resp_logout = requests.post(url=Url.url_logout(), data=self.data_logio('out_normal'), headers=headers)
            return resp_logout

    def distoken(self):  # 登录成功后获取distoken,注销时使用
        soup = BeautifulSoup(self.resp_logio(headers=Headers.headers_pc(), io='in').text, 'lxml')
        return find_md5(soup.prettify())  # 获取ditoken

    def userinfo(self, ap: str):
        if ap == 'acc':
            acc = 'XYGY_S' + self.ui.lineEdit_acc.text() + '@SCITC'  # 处理后只需输入学号即可,避免了繁琐的过程
            return acc
        elif ap == 'pwd':
            pwd = self.ui.lineEdit_pwd.text()
            return pwd

    def init_device(self):  # 初始化设备
        self.settings.remove('pc')
        self.settings.remove('phone')

    def init_logout_status(self):
        self.ui.pushButton_login_pc.setEnabled(True)
        self.ui.pushButton_login_phone.setEnabled(True)
        self.ui.pushButton_logout_pc(False)
        self.ui.pushButton_logout_phone(False)

    def basic_check(self):  # 登录检测

        if self.userinfo('acc') == '' and self.userinfo('pwd') == '':  # 进行初步判断
            QtWidgets.QMessageBox.information(self, u'错误', u'请输入用户名和密码', QtWidgets.QMessageBox.Ok)
        elif self.userinfo('acc') == '':
            QtWidgets.QMessageBox.information(self, u'错误', u'请输入用户名', QtWidgets.QMessageBox.Ok)
        elif self.userinfo('pwd') == '':
            QtWidgets.QMessageBox.information(self, u'错误', u'请输入密码', QtWidgets.QMessageBox.Ok)
        else:  # 返回True进行进阶判断
            return True

    def init_logio_button(self, device: str, io: str):
        if device == 'pc' and io == 'in':
            self.ui.pushButton_schedule_link_pc.setEnabled(True)  # 登录成功后电脑身份解锁开机自动认证按钮
            self.ui.pushButton_logout_pc.setEnabled(True)  # 解锁电脑身份注销按钮
            self.ui.pushButton_login_pc.setEnabled(False)  # 锁定电脑身份登录
            self.ui.pushButton_login_phone.setEnabled(False)  # 锁定手机身份登录
            self.ui.pushButton_schedule_link_force_cancel.setEnabled(False)  # 锁定强制取消自动登录删除
            self.ui.pushButton_schedule_link_exh.hide()  # 隐藏自动登录按钮
            self.ui.pushButton_schedule_link_cancel.hide()  # 隐藏取消自动登录按钮
            self.ui.pushButton_logout_exh.hide()  # 隐藏展示注销按钮
            self.ui.pushButton_schedule_link_phone.hide()  # 隐藏手机身份自动化登录
            self.ui.pushButton_schedule_link_force_cancel.hide()  # 隐藏强制取消自动登录
            self.ui.pushButton_schedule_link_pc.show()  # 显示电脑身份自动化登录
            self.ui.pushButton_logout_pc.show()  # 显示电脑身份注销按钮
            self.settings.setValue('Pc', 'True')
            self.settings.setValue('distoken', self.distoken())
        elif device == 'phone' and io == 'in':
            self.ui.pushButton_schedule_link_phone.setEnabled(True)  # 登录成功后解锁手机身份开机自动认证按钮
            self.ui.pushButton_logout_phone.setEnabled(True)  # 解锁手机身份注销按钮
            self.ui.pushButton_login_pc.setEnabled(False)  # 锁定电脑身份登录
            self.ui.pushButton_login_phone.setEnabled(False)  # 锁定手机身份登录
            self.ui.pushButton_schedule_link_force_cancel.setEnabled(False)  # 锁定强制取消自动登录删除
            self.ui.pushButton_schedule_link_cancel.hide()  # 隐藏取消自动登录按钮
            self.ui.pushButton_schedule_link_exh.hide()  # 隐藏自动登录按钮
            self.ui.pushButton_logout_exh.hide()  # 隐藏展示注销按钮
            self.ui.pushButton_schedule_link_pc.hide()  # 隐藏电脑身份自动化登录
            self.ui.pushButton_schedule_link_force_cancel.hide()  # 隐藏强制取消自动登录
            self.ui.pushButton_schedule_link_phone.show()  # 显示手机身份自动化登录
            self.ui.pushButton_logout_phone.show()  # 显示手机身份注销按钮
            self.settings.setValue('Phone', 'True')
            self.settings.setValue('distoken', self.distoken())
        elif device == 'pc' and io == 'out':
            self.ui.pushButton_logout_pc.setEnabled(False)  # 锁定电脑身份注销按钮
            self.ui.pushButton_schedule_link_pc.setEnabled(False)  # 锁定电脑身份开机自动登录按钮
            self.ui.pushButton_schedule_link_phone.setEnabled(False)  # 锁定手机身份开机自动登录按钮
            self.ui.pushButton_schedule_link_exh.setEnabled(False)  # 锁定开机自动登录展示按钮
            self.ui.pushButton_schedule_link_force_cancel.setEnabled(True)  # 解锁强制取消自动登录按钮
            self.ui.pushButton_login_pc.setEnabled(True)  # 解锁电脑身份登录按钮
            self.ui.pushButton_login_phone.setEnabled(True)  # 解锁手机身份登录按钮
            self.ui.pushButton_logout_phone.hide()  # 隐藏手机身份注销按钮
            self.ui.pushButton_logout_pc.hide()  # 隐藏电脑身份注销按钮(或许可以忽略不写,因为默认好像是隐藏...)
            self.ui.pushButton_schedule_link_pc.hide()  # 隐藏电脑身份开机自动登录按钮
            self.ui.pushButton_schedule_link_phone.hide()  # 隐藏手机身份开机自动登录按钮
            self.ui.pushButton_logout_exh.show()  # 显示注销登录展示按钮
            self.ui.pushButton_schedule_link_exh.show()  # 显示开机自动登录展示按钮
            self.ui.pushButton_schedule_link_force_cancel.show()  # 显示强制取消自动登录按钮
            # self.settings.setValue('pc_logout', 1)
            # self.settings.setValue('phone_logout', 0)
        elif device == 'phone' and io == 'out':
            self.ui.pushButton_logout_pc.setEnabled(False)  # 锁定电脑身份注销按钮
            self.ui.pushButton_schedule_link_pc.setEnabled(False)
            self.ui.pushButton_schedule_link_phone.setEnabled(False)
            self.ui.pushButton_schedule_link_exh.setEnabled(False)
            self.ui.pushButton_schedule_link_force_cancel.setEnabled(True)  # 解锁强制取消自动登录按钮
            self.ui.pushButton_login_pc.setEnabled(True)  # 解锁电脑身份登录按钮
            self.ui.pushButton_login_phone.setEnabled(True)  # 解锁手机身份登录按钮
            self.ui.pushButton_logout_pc.hide()
            self.ui.pushButton_logout_phone.hide()  # 或许可以忽略不写
            self.ui.pushButton_schedule_link_pc.hide()
            self.ui.pushButton_schedule_link_phone.hide()
            self.ui.pushButton_logout_exh.show()
            self.ui.pushButton_schedule_link_exh.show()  # 显示开机自动登录展示按钮
            self.ui.pushButton_schedule_link_force_cancel.show()  # 显示强制取消自动登录按钮
            # self.settings.setValue('pc_logout', 0)
            # self.settings.setValue('phone_logout', 1)

    def advance_check_pc(self):
        if self.basic_check():  # 在执行身份认证前，先进行基础检查
            if check_school_env():  # 如果当前处于校园网环境中
                connect_school_network()  # 连接校园网并等待3秒
                self.resp_logio(headers=Headers.headers_pc(), io='in')  # 是校园网就登录校园网
                if network_connection('www.baidu.com'):  # 测试网络连通性
                    self.init_device()
                    self.init_logio_button(device='pc', io='in')
                    self.tn.show_toast(title='校园网认证成功',
                                       msg=f'{find_stu_num(self.ui.lineEdit_acc.text())}' + ', ' + f'{self.hello()}' + u'认证成功！' + '\n认证身份:电脑',
                                       icon_path='./logo.ico', duration=5)
                    QtWidgets.QMessageBox.information(self, u'认证时间:' + f'{Time.now()}' + u'\t',
                                                      f'{find_stu_num(self.ui.lineEdit_acc.text())}' + ', ' + f'{self.hello()}' + u'认证成功！' + '\n认证身份:电脑',
                                                      QtWidgets.QMessageBox.Ok)

                    return find_md5(self.resp_logio(headers=Headers.headers_pc(), io='in').text)
                else:
                    QtWidgets.QMessageBox.information(self, u'错误', u'账号或密码错误', QtWidgets.QMessageBox.Ok)
            else:

                self.tn.show_toast(title=F'校园网认证失败',
                                   msg=f'{find_stu_num(self.ui.lineEdit_acc.text())}' + ',' + f'{self.hello()},' + u'当前环境非校园网认证失败！',
                                   icon_path='./logo.ico', duration=5, threaded=True)
                QtWidgets.QMessageBox.information(self, u'错误', u'当前环境非校园网', QtWidgets.QMessageBox.Ok)

    def advance_check_phone(self):  # 登录检测
        if self.basic_check():
            if check_school_env():  # 判断网络环境
                connect_school_network()  # 连接校园网并等待3秒
                self.resp_logio(headers=Headers.headers_phone(), io='in')  # 是校园网就登录校园网
                if network_connection('www.baidu.com'):  # 查看登录状态码是否为200
                    self.init_device()
                    self.init_logio_button(device='phone', io='in')
                    QtWidgets.QMessageBox.information(self, u'认证时间:' + f'{Time.now()}' + u'\t',
                                                      f'{find_stu_num(self.ui.lineEdit_acc.text())}' + ', ' + f'{self.hello()}' + u'认证成功！' + '\n认证身份:手机',
                                                      QtWidgets.QMessageBox.Ok)
                    return find_md5(self.resp_logio(headers=Headers.headers_phone(), io='in').text)
                else:
                    QtWidgets.QMessageBox.information(self, u'错误', u'登录失败', QtWidgets.QMessageBox.Ok)
            else:
                QtWidgets.QMessageBox.information(self, u'错误', u'当前环境非校园网', QtWidgets.QMessageBox.Ok)

    def logout_pc(self):
        try:
            self.resp_logio(headers=Headers.headers_pc(), io='out')
            # if not network_connection('www.baidu.com'):
            self.init_logio_button(device='pc', io='out')
            # self.init_logout_status()
            QtWidgets.QMessageBox.information(self, u'注销时间:' + f'{Time.now()}' + u'\t',
                                              f'{find_stu_num(self.ui.lineEdit_acc.text())}' + ', ' + f'{self.hello()}' + u'注销成功！' + '\n注销身份:电脑',
                                              QtWidgets.QMessageBox.Ok)
        except:
            QtWidgets.QMessageBox.information(self, u'提示', u'注销失败!', QtWidgets.QMessageBox.Ok)
        finally:
            self.init_logout_status()

    def logout_phone(self):
        try:
            self.resp_logio(headers=Headers.headers_phone(), io='out')
            # if not network_connection('www.baidu.com'):
            self.init_logio_button(device='phone', io='out')
            # self.init_logout_status()
            QtWidgets.QMessageBox.information(self, u'注销时间:' + f'{Time.now()}' + u'\t',
                                              f'{find_stu_num(self.ui.lineEdit_acc.text())}' + ', ' + f'{self.hello()}' + u'注销成功！' + '\n注销身份:手机',
                                              QtWidgets.QMessageBox.Ok)
        except:
            QtWidgets.QMessageBox.information(self, u'提示', u'注销失败!', QtWidgets.QMessageBox.Ok)
        finally:
            self.init_logout_status()

    def logout_exh(self):
        try:
            if network_connection('www.baidu.com'):
                if bool(self.settings.value('Pc') == 'True'):
                    self.resp_logio(headers=Headers.headers_pc(), io='out')
                    print('软件构造的电脑身份注销')
                    QtWidgets.QMessageBox.information(self, u'注销时间:' + f'{Time.now()}' + u'\t',
                                                      f'{self.hello()}' + u'注销成功！' + '\n注销身份:电脑',
                                                      QtWidgets.QMessageBox.Ok)

                elif bool(self.settings.value('Phone') == 'True'):
                    self.resp_logio(headers=Headers.headers_phone(), io='out')
                    print('软件构造的手机身份注销')
                    QtWidgets.QMessageBox.information(self, u'注销时间:' + f'{Time.now()}' + u'\t',
                                                      f'{self.hello()}' + u'注销成功！' + '\n注销身份:手机',
                                                      QtWidgets.QMessageBox.Ok)
                elif self.settings.value('distoken'):
                    print('正常的网页登录注销')
                    self.resp_logio(headers=Headers.headers_pc(), io='out_normal')
                    QtWidgets.QMessageBox.information(self, u'注销时间:' + f'{Time.now()}' + u'\t',
                                                      f'{self.hello()}' + u'注销成功！' + '\n注销身份:电脑',
                                                      QtWidgets.QMessageBox.Ok)
                else:
                    self.settings.setValue(f'distoken', self.distoken())
                    self.resp_logio(headers=Headers.headers_pc(), io='out_normal')
                    QtWidgets.QMessageBox.information(self, u'注销时间:' + f'{Time.now()}' + u'\t',
                                                      f'{self.hello()}' + u'注销成功！' + '\n注销身份:电脑',
                                                      QtWidgets.QMessageBox.Ok)
            else:
                QtWidgets.QMessageBox.information(self, u'提示', u'尚未联网!', QtWidgets.QMessageBox.Ok)
        except:
            QtWidgets.QMessageBox.information(self, u'提示', u'注销失败!', QtWidgets.QMessageBox.Ok)

    def make_py_local(self, headers):  # 在软件目录下创建python文件
        with open(file='schedule_link.py',
                  mode='w') as py_local:
            py_local.write(code(headers=headers, data=self.data_logio('in')))

    def make_py_startup(self, headers):  # 在startup目录下创建python登录文件
        with open(file=Dir_File.start_up_dir() + 'schedule_link.py',
                  mode='w') as py_startup:
            py_startup.write(code(headers=headers, data=self.data_logio('in')))

    def schedule_link_pc(self):
        try:
            Make_File.make_bat_startup()
            self.make_py_local(headers=Headers.headers_pc())
            if os.path.exists(
                    check_soft_env() + '\\schedule_link.py') and os.path.exists(
                Dir_File.start_up_dir() + 'schedule_link.bat') == 1:
                self.ui.pushButton_schedule_link_cancel.setEnabled(True)
                self.ui.pushButton_schedule_link_pc.hide()
                self.ui.pushButton_schedule_link_phone.hide()
                self.ui.pushButton_schedule_link_exh.hide()
                self.ui.pushButton_schedule_link_cancel.show()
                QtWidgets.QMessageBox.information(self, u'提示', u'操作成功!', QtWidgets.QMessageBox.Ok)
        except:
            if not is_admin():
                QtWidgets.QMessageBox.information(self, u'错误', u'请关闭杀毒软件软件或以管理员方式运行后重试！', QtWidgets.QMessageBox.Ok)
            else:
                QtWidgets.QMessageBox.information(self, u'错误', u'请关闭杀毒软件软件运行或后重试！', QtWidgets.QMessageBox.Ok)
        ''' 
            except:
                Make_File.make_bat_local()  # 在软件目录创建bat
                self.make_py_local()  # 在软件目录创建py
                if os.path.exists(check_soft_env() + '\\schedule_link.py') and \
                        os.path.exists(check_soft_env() + '\\schedule_link.bat') == 1:  # 检测创建的文件是否存在
                    self.ui.pushButton_schedule_link_cancel.setEnabled(True)  # 设置取消自动登录按钮为打开状态
                    reg_create(name='ScitcLinker_py', path=check_soft_env() + '\\ScitcLinker_py')  # 将py写入注册表开机目录
                    reg_create(name='ScitcLinker_bat', path=check_soft_env() + '\\ScitcLinker_bat')  # 将bat写入注册表开机目录
                    if reg_check(name='ScitcLinker_py') and reg_check(name='ScitcLinker_bat') == 1:  # 检测写入的注册表是否存在
                        QtWidgets.QMessageBox.information(self, u'提示', u'操作成功!', QtWidgets.QMessageBox.Ok)
                    else:
                        QtWidgets.QMessageBox.information(self, u'提示', u'权限不足，请以管理员方式运行或关闭杀毒软件软件后重试！')
                else:
                    QtWidgets.QMessageBox.information(self, u'提示', u'创建文件失败，请以管理员方式运行或关闭杀毒软件软件后重试！')

        else:
            QtWidgets.QMessageBox.information(self, u'错误', u'请以管理员方式运行或关闭杀毒软件软件后重试！', QtWidgets.QMessageBox.Ok)
        '''

    def schedule_link_phone(self):
        try:
            Make_File.make_bat_startup()
            self.make_py_local(headers=Headers.headers_phone())
            if os.path.exists(
                    check_soft_env() + '\\schedule_link.py') and os.path.exists(
                Dir_File.start_up_dir() + 'schedule_link.bat') == 1:
                self.ui.pushButton_schedule_link_cancel.setEnabled(True)
                self.ui.pushButton_schedule_link_pc.hide()
                self.ui.pushButton_schedule_link_phone.hide()
                self.ui.pushButton_schedule_link_exh.hide()
                self.ui.pushButton_schedule_link_cancel.show()
                QtWidgets.QMessageBox.information(self, u'提示', u'操作成功!', QtWidgets.QMessageBox.Ok)
        except:
            if not is_admin():
                QtWidgets.QMessageBox.information(self, u'错误', u'请关闭杀毒软件软件或以管理员方式运行后重试！', QtWidgets.QMessageBox.Ok)
            else:
                QtWidgets.QMessageBox.information(self, u'错误', u'请关闭杀毒软件软件运行或后重试！', QtWidgets.QMessageBox.Ok)

    def schedule_link_cancel(self):
        try:
            os.remove(Dir_File.start_up_dir() + 'schedule_link.py')
            os.remove(Dir_File.start_up_dir() + 'schedule_link.bat')
            self.ui.pushButton_schedule_link_cancel.setEnabled(False)
            self.ui.pushButton_schedule_link_exh.setEnabled(False)
            self.ui.pushButton_schedule_link_pc.setEnabled(False)
            self.ui.pushButton_schedule_link_phone.setEnabled(False)
            self.ui.pushButton_schedule_link_pc.hide()
            self.ui.pushButton_schedule_link_phone.hide()
            self.ui.pushButton_schedule_link_exh.show()
            QtWidgets.QMessageBox.information(self, u'提示', u'操作成功', QtWidgets.QMessageBox.Ok)
        except:
            QtWidgets.QMessageBox.information(self, u'错误', u'请不要使用中文目录运行软件,并关闭杀毒软件软件或以管理员方式运行后重试!',
                                              QtWidgets.QMessageBox.Ok)

    def schedule_link_force_cancel(self):  # 强制删除
        try:
            if os.path.exists(
                    Dir_File.start_up_dir() + 'schedule_link.py') and os.path.exists(
                Dir_File.start_up_dir() + 'schedule_link.bat') == 1:
                os.remove(Dir_File.start_up_dir() + 'schedule_link.py')
                os.remove(Dir_File.start_up_dir() + 'schedule_link.bat')
                self.ui.pushButton_schedule_link_force_cancel.setEnabled(False)
                self.ui.pushButton_schedule_link_cancel.setEnabled(False)
                self.ui.pushButton_schedule_link_exh.setEnabled(False)
                self.ui.pushButton_schedule_link_pc.setEnabled(False)
                self.ui.pushButton_schedule_link_phone.setEnabled(False)
                self.ui.pushButton_schedule_link_pc.hide()
                self.ui.pushButton_schedule_link_phone.hide()
                self.ui.pushButton_schedule_link_force_cancel.hide()
                self.ui.pushButton_schedule_link_exh.show()
                QtWidgets.QMessageBox.information(self, u'提示', u'操作成功', QtWidgets.QMessageBox.Ok)
            else:
                QtWidgets.QMessageBox.information(self, u'错误', u'没有自动化任务', QtWidgets.QMessageBox.Ok)
        except:
            QtWidgets.QMessageBox.information(self, u'错误', u'请不要使用中文目录运行软件,并关闭杀毒软件软件或以管理员方式运行后重试!',
                                              QtWidgets.QMessageBox.Ok)

    def save_login_info(self):  # 保存lineEdit中内容
        name = encode_base64(f'{Author_info.author_name()}')
        email = encode_base64(f'{Author_info.author_email()}')
        self.settings.setValue(f'{name}', str(bytes.decode(
            encode_base64(bytes.decode(encode_base64(self.ui.lineEdit_acc.text()))))))  # 嵌套加密账号
        self.settings.setValue(f'{email}', str(bytes.decode(
            encode_base64(bytes.decode(encode_base64(self.ui.lineEdit_pwd.text()))))))  # 嵌套加密密码

    def init_login_info(self):  # 显示上次保存的值

        name = encode_base64(f'{Author_info.author_name()}')
        email = encode_base64(f'{Author_info.author_email()}')
        the_account = decode_base64(decode_base64(self.settings.value(f'{name}', defaultValue='')))
        # the_account = decode_base64(decode_base64(self.settings.value(f'{name}',
        #                                                               defaultValue=b'V0ZsSFdWOVRRRk5EU1ZSRA==')))  # 嵌套解密账号,defaultvalue：设置初始账号，这个是base64嵌套后的，嵌套解密回来即可
        the_password = decode_base64(decode_base64(self.settings.value(f'{email}', defaultValue=b'')))  # 嵌套解密密码
        self.ui.lineEdit_acc.setText(the_account)
        self.ui.lineEdit_pwd.setText(the_password)

    def remember(self):
        if self.ui.checkBox_rem.isChecked():  # 如果勾选框被勾选
            self.save_login_info()  # 就保存lineedit中输入内容

    def show_pwd(self):  # 显示密码
        if self.ui.checkBox_show_pwd.isChecked():  # 如果勾选框被勾选
            self.ui.lineEdit_pwd.setEchoMode(QLineEdit.Normal)  # 设置lineedit编辑框的编辑模式为普通
        else:
            self.ui.lineEdit_pwd.setEchoMode(QLineEdit.Password)  # 设置lineedit编辑框的编辑模式为密码模式即****


if __name__ == '__main__':
    app = QApplication([])
    app.setWindowIcon(QIcon(':/img/img/logo.ico'))
    window = MainWindow()
    window.show()
    app.exec_()
