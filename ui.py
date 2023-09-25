# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginwHTijB.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import res_rc


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(770, 519)
        self.img_scitc_east = QLabel(Form)
        self.img_scitc_east.setObjectName(u"img_scitc_east")
        self.img_scitc_east.setGeometry(QRect(0, 1, 371, 510))
        self.img_scitc_east.setStyleSheet(u"border-image: url(:/img/img/scitc.png);\n"
                                          "border-top-left-radius: 20px;\n"
                                          "border-bottom-left-radius: 20px;\n"
                                          "")
        self.img_write_background = QLabel(Form)
        self.img_write_background.setObjectName(u"img_write_background")
        self.img_write_background.setGeometry(QRect(339, 1, 421, 510))
        self.img_write_background.setStyleSheet(u"border-top-right-radius: 20px;\n"
                                                "border-bottom-right-radius: 20px;\n"
                                                "background-color: rgb(255, 255, 255);")
        self.cabout_ui = QWidget(Form)
        self.cabout_ui.setObjectName(u"cabout_ui")
        self.cabout_ui.setGeometry(QRect(380, 101, 351, 381))
        self.lineEdit_acc = QLineEdit(self.cabout_ui)
        self.lineEdit_acc.setObjectName(u"lineEdit_acc")
        self.lineEdit_acc.setGeometry(QRect(60, 0, 251, 51))
        font = QFont()
        font.setFamily(u"\u9ed1\u4f53")
        font.setPointSize(11)
        self.lineEdit_acc.setFont(font)
        self.lineEdit_acc.setStyleSheet(u"border:1px solid rgb(170, 0, 255);\n"
                                        "border-radius:10px;")
        self.lineEdit_acc.setMaxLength(25)
        self.lineEdit_pwd = QLineEdit(self.cabout_ui)
        self.lineEdit_pwd.setObjectName(u"lineEdit_pwd")
        self.lineEdit_pwd.setGeometry(QRect(60, 70, 251, 51))
        self.lineEdit_pwd.setFont(font)
        self.lineEdit_pwd.setStyleSheet(u"border:1px solid rgb(170, 0, 255);\n"
                                        "border-radius:10px;")
        self.lineEdit_pwd.setInputMethodHints(
            Qt.ImhHiddenText | Qt.ImhNoAutoUppercase | Qt.ImhNoPredictiveText | Qt.ImhSensitiveData)
        self.lineEdit_pwd.setMaxLength(30)
        self.lineEdit_pwd.setEchoMode(QLineEdit.Password)
        self.lineEdit_pwd.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.pushButton_login_pc = QPushButton(self.cabout_ui)
        self.pushButton_login_pc.setObjectName(u"pushButton_login_pc")
        self.pushButton_login_pc.setGeometry(QRect(60, 160, 250, 45))
        font1 = QFont()
        font1.setFamily(u"\u9ed1\u4f53")
        font1.setPointSize(15)
        self.pushButton_login_pc.setFont(font1)
        self.pushButton_login_pc.setStyleSheet(u"QPushButton{\n"
                                               "background-color: rgb(170, 0, 255);\n"
                                               "border-radius:10px; \n"
                                               "color:rgb(0, 0, 0);}\n"
                                               "QPushButton:hover{background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(191, 136, 252, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                               "}\n"
                                               "QPushButton:pressed{padding-top:7px;\n"
                                               "padding-left:7px;}")
        self.pushButton_schedule_link_pc = QPushButton(self.cabout_ui)
        self.pushButton_schedule_link_pc.setObjectName(u"pushButton_schedule_link_pc")
        self.pushButton_schedule_link_pc.setGeometry(QRect(60, 325, 250, 45))
        font2 = QFont()
        font2.setFamily(u"\u9ed1\u4f53")
        font2.setPointSize(15)
        font2.setBold(False)
        font2.setWeight(50)
        self.pushButton_schedule_link_pc.setFont(font2)
        self.pushButton_schedule_link_pc.setStyleSheet(u"QPushButton{\n"
                                                       "background-color: rgb(100, 80, 255);\n"
                                                       "border-radius:10px; \n"
                                                       "color:rgb(0, 0, 0);}\n"
                                                       "QPushButton:hover{background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(166, 136, 252, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                                       "}\n"
                                                       "QPushButton:pressed{padding-top:7px;\n"
                                                       "padding-left:7px;}")
        self.pushButton_schedule_link_cancel = QPushButton(self.cabout_ui)
        self.pushButton_schedule_link_cancel.setObjectName(u"pushButton_schedule_link_cancel")
        self.pushButton_schedule_link_cancel.setGeometry(QRect(60, 325, 250, 45))
        self.pushButton_schedule_link_cancel.setFont(font2)
        self.pushButton_schedule_link_cancel.setStyleSheet(u"QPushButton{\n"
                                                           "background-color: rgb(150, 110, 255);\n"
                                                           "\n"
                                                           "border-radius:10px; \n"
                                                           "color:rgb(0, 0, 0);}\n"
                                                           "QPushButton:hover{background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(166, 136, 252, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                                           "}\n"
                                                           "QPushButton:pressed{padding-top:7px;\n"
                                                           "padding-left:7px;}")
        self.checkBox_rem = QCheckBox(self.cabout_ui)
        self.checkBox_rem.setObjectName(u"checkBox_rem")
        self.checkBox_rem.setGeometry(QRect(170, 130, 151, 21))
        font3 = QFont()
        font3.setFamily(u"\u9ed1\u4f53")
        self.checkBox_rem.setFont(font3)
        self.pushButton_login_phone = QPushButton(self.cabout_ui)
        self.pushButton_login_phone.setObjectName(u"pushButton_login_phone")
        self.pushButton_login_phone.setGeometry(QRect(60, 215, 250, 45))
        self.pushButton_login_phone.setFont(font2)
        self.pushButton_login_phone.setStyleSheet(u"QPushButton{\n"
                                                  "\n"
                                                  "background-color: rgb(135, 0, 255);\n"
                                                  "border-radius:10px; \n"
                                                  "color:rgb(0, 0, 0);}\n"
                                                  "QPushButton:hover{background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(191, 136, 252, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                                  "}\n"
                                                  "QPushButton:pressed{padding-top:7px;\n"
                                                  "padding-left:7px;}")
        self.checkBox_show_pwd = QCheckBox(self.cabout_ui)
        self.checkBox_show_pwd.setObjectName(u"checkBox_show_pwd")
        self.checkBox_show_pwd.setGeometry(QRect(65, 130, 101, 21))
        self.checkBox_show_pwd.setFont(font3)
        self.pushButton_schedule_link_phone = QPushButton(self.cabout_ui)
        self.pushButton_schedule_link_phone.setObjectName(u"pushButton_schedule_link_phone")
        self.pushButton_schedule_link_phone.setGeometry(QRect(60, 325, 250, 45))
        self.pushButton_schedule_link_phone.setFont(font2)
        self.pushButton_schedule_link_phone.setStyleSheet(u"QPushButton{\n"
                                                          "background-color: rgb(100, 80, 255);\n"
                                                          "border-radius:10px; \n"
                                                          "color:rgb(0, 0, 0);}\n"
                                                          "QPushButton:hover{background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(166, 136, 252, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                                          "}\n"
                                                          "QPushButton:pressed{padding-top:7px;\n"
                                                          "padding-left:7px;}")
        self.pushButton_schedule_link_exh = QPushButton(self.cabout_ui)
        self.pushButton_schedule_link_exh.setObjectName(u"pushButton_schedule_link_exh")
        self.pushButton_schedule_link_exh.setGeometry(QRect(60, 325, 250, 45))
        self.pushButton_schedule_link_exh.setFont(font2)
        self.pushButton_schedule_link_exh.setStyleSheet(u"QPushButton{\n"
                                                        "background-color: rgb(100, 80, 255);\n"
                                                        "border-radius:10px; \n"
                                                        "color:rgb(0, 0, 0);}\n"
                                                        "QPushButton:hover{background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(166, 136, 252, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                                        "}\n"
                                                        "QPushButton:pressed{padding-top:7px;\n"
                                                        "padding-left:7px;}")
        self.pushButton_logout_exh = QPushButton(self.cabout_ui)
        self.pushButton_logout_exh.setObjectName(u"pushButton_logout_exh")
        self.pushButton_logout_exh.setGeometry(QRect(60, 270, 250, 45))
        self.pushButton_logout_exh.setFont(font2)
        self.pushButton_logout_exh.setStyleSheet(u"QPushButton{\n"
                                                 "\n"
                                                 "background-color: rgb(125, 50, 200);\n"
                                                 "border-radius:10px; \n"
                                                 "color:rgb(0, 0, 0);}\n"
                                                 "QPushButton:hover{background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(191, 136, 252, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                                 "}\n"
                                                 "QPushButton:pressed{padding-top:7px;\n"
                                                 "padding-left:7px;}")
        self.pushButton_logout_phone = QPushButton(self.cabout_ui)
        self.pushButton_logout_phone.setObjectName(u"pushButton_logout_phone")
        self.pushButton_logout_phone.setGeometry(QRect(60, 270, 250, 45))
        self.pushButton_logout_phone.setFont(font2)
        self.pushButton_logout_phone.setStyleSheet(u"QPushButton{\n"
                                                   "\n"
                                                   "background-color: rgb(125, 50, 200);\n"
                                                   "border-radius:10px; \n"
                                                   "color:rgb(0, 0, 0);}\n"
                                                   "QPushButton:hover{background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(191, 136, 252, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                                   "}\n"
                                                   "QPushButton:pressed{padding-top:7px;\n"
                                                   "padding-left:7px;}")
        self.pushButton_logout_pc = QPushButton(self.cabout_ui)
        self.pushButton_logout_pc.setObjectName(u"pushButton_logout_pc")
        self.pushButton_logout_pc.setGeometry(QRect(60, 270, 250, 45))
        self.pushButton_logout_pc.setFont(font2)
        self.pushButton_logout_pc.setStyleSheet(u"QPushButton{\n"
                                                "\n"
                                                "background-color: rgb(125, 50, 200);\n"
                                                "border-radius:10px; \n"
                                                "color:rgb(0, 0, 0);}\n"
                                                "QPushButton:hover{background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(191, 136, 252, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                                "}\n"
                                                "QPushButton:pressed{padding-top:7px;\n"
                                                "padding-left:7px;}")
        self.pushButton_schedule_link_force_cancel = QPushButton(self.cabout_ui)
        self.pushButton_schedule_link_force_cancel.setObjectName(u"pushButton_schedule_link_force_cancel")
        self.pushButton_schedule_link_force_cancel.setGeometry(QRect(60, 325, 250, 45))
        self.pushButton_schedule_link_force_cancel.setFont(font2)
        self.pushButton_schedule_link_force_cancel.setStyleSheet(u"QPushButton{\n"
                                                                 "background-color: rgb(100, 80, 255);\n"
                                                                 "border-radius:10px; \n"
                                                                 "color:rgb(0, 0, 0);}\n"
                                                                 "QPushButton:hover{background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(166, 136, 252, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                                                 "}\n"
                                                                 "QPushButton:pressed{padding-top:7px;\n"
                                                                 "padding-left:7px;}")
        self.lineEdit_pwd.raise_()
        self.lineEdit_acc.raise_()
        self.pushButton_login_pc.raise_()
        self.pushButton_schedule_link_pc.raise_()
        self.pushButton_schedule_link_cancel.raise_()
        self.checkBox_rem.raise_()
        self.pushButton_login_phone.raise_()
        self.checkBox_show_pwd.raise_()
        self.pushButton_schedule_link_phone.raise_()
        self.pushButton_schedule_link_exh.raise_()
        self.pushButton_logout_exh.raise_()
        self.pushButton_logout_phone.raise_()
        self.pushButton_logout_pc.raise_()
        self.pushButton_schedule_link_force_cancel.raise_()
        self.pushButton_quit = QPushButton(Form)
        self.pushButton_quit.setObjectName(u"pushButton_quit")
        self.pushButton_quit.setGeometry(QRect(710, 11, 31, 28))
        font4 = QFont()
        font4.setFamily(u"Arial")
        self.pushButton_quit.setFont(font4)
        self.pushButton_quit.setStyleSheet(u"QPushButton{\n"
                                           "background-color: rgbA(0, 0, 0, 255);\n"
                                           "border-radius:10px; \n"
                                           "color:rgb(0, 0, 0);}\n"
                                           "QPushButton:hover{background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                           "}\n"
                                           "QPushButton:pressed{padding-top:7px;\n"
                                           "padding-left:7px;}")
        self.pushButton_mini = QPushButton(Form)
        self.pushButton_mini.setObjectName(u"pushButton_mini")
        self.pushButton_mini.setGeometry(QRect(670, 11, 31, 28))
        font5 = QFont()
        font5.setFamily(u"Arial")
        font5.setPointSize(13)
        self.pushButton_mini.setFont(font5)
        self.pushButton_mini.setStyleSheet(u"QPushButton{\n"
                                           "background-color: rgbA(0, 0, 0, 255);\n"
                                           "border-radius:10px; \n"
                                           "color:rgb(0, 0, 0);}\n"
                                           "QPushButton:hover{background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 222, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                           "}\n"
                                           "QPushButton:pressed{padding-top:7px;\n"
                                           "padding-left:7px;}")
        self.clogin_ui = QWidget(Form)
        self.clogin_ui.setObjectName(u"clogin_ui")
        self.clogin_ui.setGeometry(QRect(460, 46, 215, 50))
        self.horizontalLayout_2 = QHBoxLayout(self.clogin_ui)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_clogin = QPushButton(self.clogin_ui)
        self.pushButton_clogin.setObjectName(u"pushButton_clogin")
        font6 = QFont()
        font6.setFamily(u"\u9ed1\u4f53")
        font6.setPointSize(12)
        self.pushButton_clogin.setFont(font6)
        self.pushButton_clogin.setStyleSheet(u"#pushButton_clogin{\n"
                                             "border:none;\n"
                                             "color:rgb(170, 0, 255);\n"
                                             "}\n"
                                             "#pushButton:focus {\n"
                                             "	color:gray;\n"
                                             "}\n"
                                             "")

        self.horizontalLayout_2.addWidget(self.pushButton_clogin)

        self.line = QFrame(self.clogin_ui)
        self.line.setObjectName(u"line")
        font7 = QFont()
        font7.setBold(True)
        font7.setWeight(75)
        self.line.setFont(font7)
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line)

        self.pushButton_cabout = QPushButton(self.clogin_ui)
        self.pushButton_cabout.setObjectName(u"pushButton_cabout")
        self.pushButton_cabout.setFont(font6)
        self.pushButton_cabout.setStyleSheet(u"#pushButton_cabout{\n"
                                             "border:none;\n"
                                             "color:rgb(170, 0, 255);\n"
                                             "}\n"
                                             "#pushButton:focus {\n"
                                             "	color:gray;\n"
                                             "}\n"
                                             "")

        self.horizontalLayout_2.addWidget(self.pushButton_cabout)

        self.money_ui = QWidget(Form)
        self.money_ui.setObjectName(u"money_ui")
        self.money_ui.setGeometry(QRect(-20, -10, 791, 522))
        self.img_scitc_playground = QLabel(self.money_ui)
        self.img_scitc_playground.setObjectName(u"img_scitc_playground")
        self.img_scitc_playground.setGeometry(QRect(20, 10, 761, 511))
        self.img_scitc_playground.setStyleSheet(u"border-top-left-radius: 20px;\n"
                                                "border-bottom-left-radius: 20px;\n"
                                                "border-top-right-radius: 20px;\n"
                                                "border-bottom-right-radius: 20px;\n"
                                                "border-image: url(:/img/img/zz.png);")
        self.pushButton_back = QPushButton(self.money_ui)
        self.pushButton_back.setObjectName(u"pushButton_back")
        self.pushButton_back.setGeometry(QRect(430, 370, 130, 80))
        font8 = QFont()
        font8.setFamily(u"\u9ed1\u4f53")
        font8.setPointSize(12)
        font8.setBold(False)
        font8.setWeight(50)
        self.pushButton_back.setFont(font8)
        self.pushButton_back.setStyleSheet(u"QPushButton{\n"
                                           "\n"
                                           "background-color: rgb(97, 139, 255);\n"
                                           "\n"
                                           "border-radius:10px; \n"
                                           "color:rgb(0, 0, 0);}\n"
                                           "QPushButton:hover{background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(162, 192, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                           "}")
        self.pushButton_money = QPushButton(self.money_ui)
        self.pushButton_money.setObjectName(u"pushButton_money")
        self.pushButton_money.setEnabled(True)
        self.pushButton_money.setGeometry(QRect(230, 370, 130, 80))
        self.pushButton_money.setFont(font8)
        self.pushButton_money.setStyleSheet(u"QPushButton{\n"
                                            "\n"
                                            "	background-color: rgb(187, 255, 78);\n"
                                            "border-radius:10px; \n"
                                            "color: rgb(0, 0, 0);}\n"
                                            "QPushButton:hover{background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 177, 207, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                            "}")
        self.pushButton_money.setIconSize(QSize(20, 20))
        self.img_pay = QLabel(self.money_ui)
        self.img_pay.setObjectName(u"img_pay")
        self.img_pay.setGeometry(QRect(100, 10, 601, 341))
        self.img_pay.setStyleSheet(u"border-image: url(:/img/img/wxzfb.png);\n"
                                   "border-top-left-radius: 20px;\n"
                                   "border-bottom-left-radius: 20px;\n"
                                   "border-top-right-radius: 20px;\n"
                                   "border-bottom-right-radius: 20px;")
        self.pushButton_quit_pay = QPushButton(self.money_ui)
        self.pushButton_quit_pay.setObjectName(u"pushButton_quit_pay")
        self.pushButton_quit_pay.setGeometry(QRect(660, 10, 41, 41))
        font9 = QFont()
        font9.setFamily(u"\u9ed1\u4f53")
        font9.setPointSize(10)
        font9.setBold(False)
        font9.setWeight(50)
        self.pushButton_quit_pay.setFont(font9)
        self.pushButton_quit_pay.setStyleSheet(u"QPushButton{\n"
                                               "\n"
                                               "	background-color: rgb(244, 0, 0);\n"
                                               "border-radius:10px; \n"
                                               "color: rgb(0, 0, 0);}\n"
                                               "QPushButton:hover{background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 177, 207, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                               "}")
        self.pushButton_qq = QPushButton(self.money_ui)
        self.pushButton_qq.setObjectName(u"pushButton_qq")
        self.pushButton_qq.setGeometry(QRect(300, 110, 30, 30))
        font10 = QFont()
        font10.setFamily(u"\u9ed1\u4f53")
        font10.setPointSize(30)
        font10.setBold(True)
        font10.setWeight(75)
        self.pushButton_qq.setFont(font10)
        self.pushButton_qq.setStyleSheet(u"#pushButton_qq{\n"
                                         "	image: url(:/img/img/favicon_q.ico);\n"
                                         "border:none;\n"
                                         "color:rgb(252, 157, 154);\n"
                                         "}\n"
                                         "#pushButton:focus {\n"
                                         "	color:gray;\n"
                                         "}\n"
                                         "\n"
                                         "")
        self.pushButton_bilibili = QPushButton(self.money_ui)
        self.pushButton_bilibili.setObjectName(u"pushButton_bilibili")
        self.pushButton_bilibili.setGeometry(QRect(350, 110, 30, 30))
        font11 = QFont()
        font11.setFamily(u"\u9ed1\u4f53")
        font11.setPointSize(30)
        self.pushButton_bilibili.setFont(font11)
        self.pushButton_bilibili.setStyleSheet(u"	#pushButton_bilibili{\n"
                                               "	image: url(:/img/img/favicon_b.ico);\n"
                                               "border:none;\n"
                                               "color:rgb(200, 200, 169);\n"
                                               "}\n"
                                               "#pushButton:focus {\n"
                                               "	color:gray;\n"
                                               "}\n"
                                               "\n"
                                               "")
        self.pushButton_tips = QPushButton(self.money_ui)
        self.pushButton_tips.setObjectName(u"pushButton_tips")
        self.pushButton_tips.setGeometry(QRect(100, 30, 601, 50))
        font12 = QFont()
        font12.setFamily(u"\u9ed1\u4f53")
        font12.setPointSize(23)
        font12.setBold(False)
        font12.setWeight(50)
        self.pushButton_tips.setFont(font12)
        self.pushButton_tips.setAutoFillBackground(False)
        self.pushButton_tips.setStyleSheet(u"#pushButton_tips{\n"
                                           "border:none;\n"
                                           "	\n"
                                           "	color: rgb(167, 117, 60);\n"
                                           "}\n"
                                           "#pushButton:focus {\n"
                                           "	color:gray;\n"
                                           "}\n"
                                           "")
        self.pushButton_douyin = QPushButton(self.money_ui)
        self.pushButton_douyin.setObjectName(u"pushButton_douyin")
        self.pushButton_douyin.setGeometry(QRect(400, 110, 30, 30))
        self.pushButton_douyin.setFont(font10)
        self.pushButton_douyin.setStyleSheet(u"#pushButton_douyin{\n"
                                             "	image: url(:/img/img/favicon_d.ico);\n"
                                             "border:none;\n"
                                             "color:rgb(249, 205, 173);\n"
                                             "}\n"
                                             "#pushButton:focus {\n"
                                             "	color:gray;\n"
                                             "}\n"
                                             "\n"
                                             "")
        self.pushButton_kuaishou = QPushButton(self.money_ui)
        self.pushButton_kuaishou.setObjectName(u"pushButton_kuaishou")
        self.pushButton_kuaishou.setGeometry(QRect(450, 110, 30, 30))
        self.pushButton_kuaishou.setFont(font11)
        self.pushButton_kuaishou.setStyleSheet(u"#pushButton_kuaishou{\n"
                                               "	image: url(:/img/img/favicon_k.ico);\n"
                                               "border:none;\n"
                                               "color:rgb(131, 175, 155);\n"
                                               "}\n"
                                               "#pushButton:focus {\n"
                                               "	color:gray;\n"
                                               "}\n"
                                               "\n"
                                               "")
        self.pushButton_author = QPushButton(self.money_ui)
        self.pushButton_author.setObjectName(u"pushButton_author")
        self.pushButton_author.setGeometry(QRect(100, 145, 601, 211))
        self.pushButton_author.setFont(font12)
        self.pushButton_author.setAutoFillBackground(False)
        self.pushButton_author.setStyleSheet(u"#pushButton_author{\n"
                                             "border:none;\n"
                                             "color:\n"
                                             "             qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                             "                                stop: 0 #c5ff49, stop: 0.4 #a1ff75,\n"
                                             "                                stop: 0.5 #b0dd5d, stop: 1.0 #fddc21)\n"
                                             "}\n"
                                             "#pushButton:focus {\n"
                                             "	color:gray;\n"
                                             "}\n"
                                             "")
        self.img_write_background.raise_()
        self.img_scitc_east.raise_()
        self.money_ui.raise_()
        self.cabout_ui.raise_()
        self.clogin_ui.raise_()
        self.pushButton_quit.raise_()
        self.pushButton_mini.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u5ddd\u4fe1\u7f51\u7edc\u8ba4\u8bc1", None))
        self.img_scitc_east.setText("")
        self.img_write_background.setText("")
        self.lineEdit_acc.setPlaceholderText(QCoreApplication.translate("Form", u"\u8d26\u53f7:", None))
        self.lineEdit_pwd.setPlaceholderText(QCoreApplication.translate("Form", u"\u5bc6\u7801:", None))
        self.pushButton_login_pc.setText(QCoreApplication.translate("Form", u"\u767b  \u5f55", None))
        self.pushButton_schedule_link_pc.setText(
            QCoreApplication.translate("Form", u"\u81ea\u52a8\u8ba4\u8bc1(\u7535\u8111)", None))
        self.pushButton_schedule_link_cancel.setText(
            QCoreApplication.translate("Form", u"\u53d6\u6d88\u81ea\u52a8\u8ba4\u8bc1", None))
        self.checkBox_rem.setText(QCoreApplication.translate("Form", u"\u8bb0\u4f4f\u8d26\u53f7\u5bc6\u7801", None))
        self.pushButton_login_phone.setText(
            QCoreApplication.translate("Form", u"\u4f2a\u88c5\u624b\u673a\u767b\u5f55", None))
        self.checkBox_show_pwd.setText(QCoreApplication.translate("Form", u"\u663e\u793a\u5bc6\u7801", None))
        self.pushButton_schedule_link_phone.setText(
            QCoreApplication.translate("Form", u"\u81ea\u52a8\u8ba4\u8bc1(\u624b\u673a)", None))
        self.pushButton_schedule_link_exh.setText(QCoreApplication.translate("Form", u"\u81ea\u52a8\u8ba4\u8bc1", None))
        self.pushButton_logout_exh.setText(QCoreApplication.translate("Form", u"\u6ce8  \u9500", None))
        self.pushButton_logout_phone.setText(QCoreApplication.translate("Form", u"\u6ce8\u9500(\u624b\u673a)", None))
        self.pushButton_logout_pc.setText(QCoreApplication.translate("Form", u"\u6ce8\u9500(\u7535\u8111)", None))
        self.pushButton_schedule_link_force_cancel.setText(
            QCoreApplication.translate("Form", u"\u5f3a\u5236\u53d6\u6d88\u81ea\u52a8\u8ba4\u8bc1", None))
        self.pushButton_quit.setText(QCoreApplication.translate("Form", u"X", None))
        self.pushButton_mini.setText(QCoreApplication.translate("Form", u"-", None))
        self.pushButton_clogin.setText(QCoreApplication.translate("Form", u"\u767b\u5f55", None))
        self.pushButton_cabout.setText(QCoreApplication.translate("Form", u"\u5173\u4e8e\u4f5c\u8005", None))
        self.img_scitc_playground.setText("")
        self.pushButton_back.setText(QCoreApplication.translate("Form", u"\u8fd4\u56de\u4e3b\u9875", None))
        self.pushButton_money.setText(QCoreApplication.translate("Form", u"\u6350\u8d60\u4f5c\u8005", None))
        self.img_pay.setText("")
        self.pushButton_quit_pay.setText(QCoreApplication.translate("Form", u"\u5173\u95ed", None))
        self.pushButton_qq.setText("")
        self.pushButton_bilibili.setText("")
        self.pushButton_tips.setText(QCoreApplication.translate("Form",
                                                                u"\u5173\u4e8e\u4f5c\u8005(\u70b9\u51fb\u56fe\u6807\u5373\u53ef\u6dfb\u52a0)",
                                                                None))
        self.pushButton_douyin.setText("")
        self.pushButton_kuaishou.setText("")
        self.pushButton_author.setText(
            QCoreApplication.translate("Form", u"\u552f\u4e00\u4f5c\u8005\uff1aLZY/\u6211\u4e0d\u662f\u76d8\u795e\n"
                                               "\u6709\u4efb\u4f55\u95ee\u9898\u8bf7\u8054\u7cfb\u4f5c\u8005\n"
                                               "\u672a\u7ecf\u5141\u8bb8\uff0c\u7981\u6b62\u8f6c\u8f7d\u3001\u76d7\u5356",
                                       None))
    # retranslateUi
