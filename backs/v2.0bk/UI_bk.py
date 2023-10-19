from PyQt5 import QtCore, QtGui, QtWidgets

import math
import os
import sys

from PyQt5.QtGui import QFontDatabase

import res_rc
from enemy import *
from heart import *
from calculation_formula import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(551, 480)
        main_icon = QtGui.QIcon()
        main_icon.addPixmap(QtGui.QPixmap(':resources/images/logo_yellow.ico'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(main_icon)
        fontDb = QFontDatabase()
        fontID = fontDb.addApplicationFont(":resources/font/hana_simplify.ttf")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.all_frame = QtWidgets.QFrame(self.centralwidget)
        self.all_frame.setGeometry(QtCore.QRect(10, 10, 531, 461))
        self.all_frame.setStyleSheet("#all_frame\n"
                                     "{\n"
                                     "    background:#272727;\n"
                                     "    border-radius:12px;\n"
                                     "}\n"
                                     "\n"
                                     "#calculate_button\n"
                                     "{\n"
                                     "    font-family:\"HanaMinA\";\n"
                                     "    color:#99795C;\n"
                                     "    background:#B5B3AF;\n"
                                     "    font-size:15px;\n"
                                     "    font-weight:bold;\n"
                                     "    \n"
                                     "}\n"
                                     "\n"
                                     "QLabel\n"
                                     "{\n"
                                     "    color: #99795C;\n"
                                     "    font-weight:bold;\n"
                                     "    font-family:\"HanaMinA\";\n"
                                     "    font-size:15px;\n"
                                     "}\n"
                                     "\n"
                                     "QLineEdit\n"
                                     "{    \n"
                                     "    background:#242524;\n"
                                     "    border:0px;\n"
                                     "    border-bottom: 1px solid #99795C;\n"
                                     "    color: #BEBAB8;\n"
                                     "    font-size:15px;\n"
                                     "    font-weight:bold;\n"
                                     "    font-family:\"HanaMinA\";\n"
                                     "\n"
                                     "}\n"
                                     "\n"
                                     "\n"
                                     "\n"
                                     "QTextEdit\n"
                                     "{    \n"
                                     "    border-radius:7px;\n"
                                     "    border:0px;\n"
                                     "    background:#D5D3CF;\n"
                                     "    font-size:13px;\n"
                                     "    font-weight:bold;\n"
                                     "    font-family:\"HanaMinA\";\n"
                                     "    color:#464F47;\n"
                                     "}\n"
                                     "\n"
                                     "QComboBox\n"
                                     "{\n"
                                     "    font-size:12px;\n"
                                     "    font-family:\"HanaMinA\";\n"
                                     "    font-weight:bold;\n"
                                     "    color:#BEBAB8;\n"
                                     "    background:#242524;\n"
                                     "    border: 1px solid #99795C; \n"
                                     "    border-radius:4px;\n"
                                     "}\n"
                                     "\n"
                                     "\n"
                                     "\n"
                                     "QComboBox QAbstractItemView \n"
                                     "{    \n"
                                     "    font-size:12px;\n"
                                     "    font-family:\"HanaMinA\";\n"
                                     "    font-weight:bold;\n"
                                     "    \n"
                                     "    outline: 0px solid gray;  \n"
                                     "    border: 1px solid #99795C;\n"
                                     "    border-radius:4px;    \n"
                                     "    \n"
                                     "    color:#BEBAB8;\n"
                                     "    background-color: #242524;   \n"
                                     "    selection-background-color: #BEBAB8;   \n"
                                     "}\n"
                                     "\n"
                                     "\n"
                                     "QComboBox::drop-down \n"
                                     "{\n"
                                     "    border:none;\n"
                                     "}\n"
                                     "\n"
                                     "\n"
                                     "")
        self.all_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.all_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.all_frame.setObjectName("all_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.all_frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.top_frame = QtWidgets.QFrame(self.all_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.top_frame.sizePolicy().hasHeightForWidth())
        self.top_frame.setSizePolicy(sizePolicy)
        self.top_frame.setStyleSheet("#top_frame{\n"
                                     "\n"
                                     "border-top-left-radius:12px;\n"
                                     "border-top-right-radius:12px\n"
                                     "}")
        self.top_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_frame.setObjectName("top_frame")
        self.button_frame = QtWidgets.QFrame(self.top_frame)
        self.button_frame.setGeometry(QtCore.QRect(400, 0, 131, 51))
        self.button_frame.setStyleSheet("\n"
                                        "QPushButton{\n"
                                        "border:none;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "padding-botton:5px\n"
                                        "}")
        self.button_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.button_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.button_frame.setObjectName("button_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.button_frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushbutton_min = QtWidgets.QPushButton(self.button_frame)
        self.pushbutton_min.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(':resources/images/min.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushbutton_min.setIcon(icon)
        self.pushbutton_min.setObjectName("pushbutton_min")
        self.horizontalLayout_2.addWidget(self.pushbutton_min)
        self.pushbutton_max = QtWidgets.QPushButton(self.button_frame)
        self.pushbutton_max.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(':resources/images/max.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(':resources/images/return.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushbutton_max.setIcon(icon1)
        self.pushbutton_max.setObjectName("pushbutton_max")
        self.pushbutton_max.setCheckable(True)
        self.horizontalLayout_2.addWidget(self.pushbutton_max)
        self.pushbutton_close = QtWidgets.QPushButton(self.button_frame)
        self.pushbutton_close.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(':resources/images/close.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushbutton_close.setIcon(icon2)
        self.pushbutton_close.setAutoDefault(False)
        self.pushbutton_close.setObjectName("pushbutton_close")
        self.horizontalLayout_2.addWidget(self.pushbutton_close)
        self.logo_frame = QtWidgets.QFrame(self.top_frame)
        self.logo_frame.setGeometry(QtCore.QRect(10, 0, 131, 61))
        self.logo_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.logo_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.logo_frame.setObjectName("logo_frame")
        self.logo_label_2 = QtWidgets.QLabel(self.logo_frame)
        self.logo_label_2.setGeometry(QtCore.QRect(0, 0, 131, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo_label_2.sizePolicy().hasHeightForWidth())
        self.logo_label_2.setSizePolicy(sizePolicy)
        self.logo_label_2.setText("")
        self.logo_label_2.setPixmap(QtGui.QPixmap(':resources/images/logo_yellow.ico'))
        self.logo_label_2.setObjectName("logo_label_2")
        self.verticalLayout.addWidget(self.top_frame)
        self.main_frame = QtWidgets.QFrame(self.all_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(7)
        sizePolicy.setHeightForWidth(self.main_frame.sizePolicy().hasHeightForWidth())
        self.main_frame.setSizePolicy(sizePolicy)
        self.main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame.setObjectName("main_frame")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.main_frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 151, 51))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.attack_input_Layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.attack_input_Layout.setContentsMargins(0, 0, 0, 0)
        self.attack_input_Layout.setObjectName("attack_input_Layout")
        self.attack_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("HanaMinA")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.attack_label.setFont(font)
        self.attack_label.setToolTip("")
        self.attack_label.setObjectName("attack_label")
        self.attack_input_Layout.addWidget(self.attack_label)
        self.attack_input = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.attack_input.setObjectName("attack_input")
        self.attack_input_Layout.addWidget(self.attack_input)
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.main_frame)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(10, 60, 151, 53))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.critical_strike_rate_input_Layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.critical_strike_rate_input_Layout.setContentsMargins(0, 0, 0, 0)
        self.critical_strike_rate_input_Layout.setObjectName("critical_strike_rate_input_Layout")
        self.critical_strike_rate_label = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("HanaMinA")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.critical_strike_rate_label.setFont(font)
        self.critical_strike_rate_label.setToolTip("")
        self.critical_strike_rate_label.setObjectName("critical_strike_rate_label")
        self.critical_strike_rate_input_Layout.addWidget(self.critical_strike_rate_label)
        self.input_Layout_3 = QtWidgets.QHBoxLayout()
        self.input_Layout_3.setObjectName("input_Layout_3")
        self.critical_strike_rate_input = QtWidgets.QLineEdit(self.verticalLayoutWidget_5)
        self.critical_strike_rate_input.setObjectName("critical_strike_rate_input")
        self.input_Layout_3.addWidget(self.critical_strike_rate_input)
        self.sign_3 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.sign_3.setObjectName("sign_3")
        self.input_Layout_3.addWidget(self.sign_3)
        self.critical_strike_rate_input_Layout.addLayout(self.input_Layout_3)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.main_frame)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(170, 10, 151, 53))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.skill_ratio_input_Layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.skill_ratio_input_Layout.setContentsMargins(0, 0, 0, 0)
        self.skill_ratio_input_Layout.setObjectName("skill_ratio_input_Layout")
        self.skill_ratio_laber = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("HanaMinA")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.skill_ratio_laber.setFont(font)
        self.skill_ratio_laber.setToolTip("")
        self.skill_ratio_laber.setObjectName("skill_ratio_laber")
        self.skill_ratio_input_Layout.addWidget(self.skill_ratio_laber)
        self.input_Layout_1 = QtWidgets.QHBoxLayout()
        self.input_Layout_1.setObjectName("input_Layout_1")
        self.skill_ratio_input = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.skill_ratio_input.setObjectName("skill_ratio_input")
        self.input_Layout_1.addWidget(self.skill_ratio_input)
        self.sign_1 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.sign_1.setObjectName("sign_1")
        self.input_Layout_1.addWidget(self.sign_1)
        self.skill_ratio_input_Layout.addLayout(self.input_Layout_1)
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.main_frame)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(170, 60, 151, 53))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.critical_strike_ratio_input_Layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.critical_strike_ratio_input_Layout.setContentsMargins(0, 0, 0, 0)
        self.critical_strike_ratio_input_Layout.setObjectName("critical_strike_ratio_input_Layout")
        self.critical_strike_ratio_label = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        font = QtGui.QFont()
        font.setFamily("HanaMinA")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.critical_strike_ratio_label.setFont(font)
        self.critical_strike_ratio_label.setToolTip("")
        self.critical_strike_ratio_label.setObjectName("critical_strike_ratio_label")
        self.critical_strike_ratio_input_Layout.addWidget(self.critical_strike_ratio_label)
        self.input_Layout_4 = QtWidgets.QHBoxLayout()
        self.input_Layout_4.setObjectName("input_Layout_4")
        self.critical_strike_ratio_input = QtWidgets.QLineEdit(self.verticalLayoutWidget_6)
        self.critical_strike_ratio_input.setObjectName("critical_strike_ratio_input")
        self.input_Layout_4.addWidget(self.critical_strike_ratio_input)
        self.sign_4 = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        self.sign_4.setObjectName("sign_4")
        self.input_Layout_4.addWidget(self.sign_4)
        self.critical_strike_ratio_input_Layout.addLayout(self.input_Layout_4)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.main_frame)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(10, 110, 151, 53))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.damage_increase_input_Layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.damage_increase_input_Layout.setContentsMargins(0, 0, 0, 0)
        self.damage_increase_input_Layout.setObjectName("damage_increase_input_Layout")
        self.damage_increase_label = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("HanaMinA")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.damage_increase_label.setFont(font)
        self.damage_increase_label.setToolTip("")
        self.damage_increase_label.setObjectName("damage_increase_label")
        self.damage_increase_input_Layout.addWidget(self.damage_increase_label)
        self.input_Layout_2 = QtWidgets.QHBoxLayout()
        self.input_Layout_2.setObjectName("input_Layout_2")
        self.damage_increase_input = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.damage_increase_input.setObjectName("damage_increase_input")
        self.input_Layout_2.addWidget(self.damage_increase_input)
        self.sign_2 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.sign_2.setObjectName("sign_2")
        self.input_Layout_2.addWidget(self.sign_2)
        self.damage_increase_input_Layout.addLayout(self.input_Layout_2)
        self.verticalLayoutWidget_8 = QtWidgets.QWidget(self.main_frame)
        self.verticalLayoutWidget_8.setGeometry(QtCore.QRect(170, 110, 151, 48))
        self.verticalLayoutWidget_8.setObjectName("verticalLayoutWidget_8")
        self.matchup_choice_combobox_Layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_8)
        self.matchup_choice_combobox_Layout.setContentsMargins(0, 0, 0, 0)
        self.matchup_choice_combobox_Layout.setObjectName("matchup_choice_combobox_Layout")
        self.matchup_choice_label = QtWidgets.QLabel(self.verticalLayoutWidget_8)
        font = QtGui.QFont()
        font.setFamily("HanaMinA")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.matchup_choice_label.setFont(font)
        self.matchup_choice_label.setToolTip("")
        self.matchup_choice_label.setObjectName("matchup_choice_label")
        self.matchup_choice_combobox_Layout.addWidget(self.matchup_choice_label)
        self.matchup_choice_combobox = QtWidgets.QComboBox(self.verticalLayoutWidget_8)
        self.matchup_choice_combobox.setObjectName("matchup_choice_combobox")
        self.matchup_choice_combobox.addItem("")
        self.matchup_choice_combobox.addItem("")
        self.matchup_choice_combobox_Layout.addWidget(self.matchup_choice_combobox)
        self.verticalLayoutWidget_7 = QtWidgets.QWidget(self.main_frame)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(10, 160, 151, 48))
        self.verticalLayoutWidget_7.setObjectName("verticalLayoutWidget_7")
        self.skill_choice_combobox_Layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_7)
        self.skill_choice_combobox_Layout.setContentsMargins(0, 0, 0, 0)
        self.skill_choice_combobox_Layout.setObjectName("skill_choice_combobox_Layout")
        self.skill_choice_label = QtWidgets.QLabel(self.verticalLayoutWidget_7)
        font = QtGui.QFont()
        font.setFamily("HanaMinA")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.skill_choice_label.setFont(font)
        self.skill_choice_label.setToolTip("")
        self.skill_choice_label.setObjectName("skill_choice_label")
        self.skill_choice_combobox_Layout.addWidget(self.skill_choice_label)
        self.skill_choice_combobox = QtWidgets.QComboBox(self.verticalLayoutWidget_7)
        self.skill_choice_combobox.setObjectName("skill_choice_combobox")
        self.skill_choice_combobox.addItem("")
        self.skill_choice_combobox.addItem("")
        self.skill_choice_combobox_Layout.addWidget(self.skill_choice_combobox)
        self.verticalLayoutWidget_9 = QtWidgets.QWidget(self.main_frame)
        self.verticalLayoutWidget_9.setGeometry(QtCore.QRect(170, 160, 151, 48))
        self.verticalLayoutWidget_9.setObjectName("verticalLayoutWidget_9")
        self.damage_choice_combobox_Layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_9)
        self.damage_choice_combobox_Layout.setContentsMargins(0, 0, 0, 0)
        self.damage_choice_combobox_Layout.setObjectName("damage_choice_combobox_Layout")
        self.damage_choice_label = QtWidgets.QLabel(self.verticalLayoutWidget_9)
        font = QtGui.QFont()
        font.setFamily("HanaMinA")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.damage_choice_label.setFont(font)
        self.damage_choice_label.setToolTip("")
        self.damage_choice_label.setObjectName("damage_choice_label")
        self.damage_choice_combobox_Layout.addWidget(self.damage_choice_label)
        self.damage_choice_combobox = QtWidgets.QComboBox(self.verticalLayoutWidget_9)
        self.damage_choice_combobox.setObjectName("damage_choice_combobox")
        self.damage_choice_combobox.addItem("")
        self.damage_choice_combobox.addItem("")
        self.damage_choice_combobox_Layout.addWidget(self.damage_choice_combobox)
        self.verticalLayoutWidget_10 = QtWidgets.QWidget(self.main_frame)
        self.verticalLayoutWidget_10.setGeometry(QtCore.QRect(10, 210, 151, 94))
        self.verticalLayoutWidget_10.setObjectName("verticalLayoutWidget_10")
        self.heart_choice_combobox_Layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_10)
        self.heart_choice_combobox_Layout.setContentsMargins(0, 0, 0, 0)
        self.heart_choice_combobox_Layout.setObjectName("heart_choice_combobox_Layout")
        self.heart_choice_combobox_label = QtWidgets.QLabel(self.verticalLayoutWidget_10)
        font = QtGui.QFont()
        font.setFamily("HanaMinA")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.heart_choice_combobox_label.setFont(font)
        self.heart_choice_combobox_label.setToolTip("")
        self.heart_choice_combobox_label.setObjectName("heart_choice_combobox_label")
        global heart
        heart = choice_heart(0)
        self.heart_choice_combobox_Layout.addWidget(self.heart_choice_combobox_label)
        self.heart_choice_combobox = QtWidgets.QComboBox(self.verticalLayoutWidget_10)
        self.heart_choice_combobox.setIconSize(QtCore.QSize(60, 60))
        self.heart_choice_combobox.setObjectName("heart_choice_combobox")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(':resources/images/1.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.heart_choice_combobox.addItem(icon3, "")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(':resources/images/2.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.heart_choice_combobox.addItem(icon4, "")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(':resources/images/3.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.heart_choice_combobox.addItem(icon5, "")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(':resources/images/4.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.heart_choice_combobox.addItem(icon6, "")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(':resources/images/5.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.heart_choice_combobox.addItem(icon7, "")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(':resources/images/6.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.heart_choice_combobox.addItem(icon8, "")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(':resources/images/7.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.heart_choice_combobox.addItem(icon9, "")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(':resources/images/8.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.heart_choice_combobox.addItem(icon10, "")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(':resources/images/9.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.heart_choice_combobox.addItem(icon11, "")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(':resources/images/10.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.heart_choice_combobox.addItem(icon12, "")
        self.heart_choice_combobox.currentIndexChanged.connect(self.update_heart)
        self.heart_choice_combobox_Layout.addWidget(self.heart_choice_combobox)
        self.heart_info_text = QtWidgets.QTextEdit(self.main_frame)

        data_heart = f"心相攻击力：{heart.heart_attack}\n仪式加成：{heart.ritual_power * 100}%\n术法加成：{heart.magic_power * 100}%\n创伤加成：{heart.damage_bonus * 100}%"
        self.heart_info_text.setPlainText(data_heart)
        self.heart_info_text.setGeometry(QtCore.QRect(170, 210, 151, 81))
        self.heart_info_text.setReadOnly(True)
        self.heart_info_text.setObjectName("heart_info_text")
        self.verticalLayoutWidget_11 = QtWidgets.QWidget(self.main_frame)
        self.verticalLayoutWidget_11.setGeometry(QtCore.QRect(10, 300, 151, 71))
        self.verticalLayoutWidget_11.setObjectName("verticalLayoutWidget_11")
        self.enemy_choice_combobox_Layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_11)
        self.enemy_choice_combobox_Layout.setContentsMargins(0, 0, 0, 0)
        self.enemy_choice_combobox_Layout.setObjectName("enemy_choice_combobox_Layout")
        self.enemy_choice_label = QtWidgets.QLabel(self.verticalLayoutWidget_11)
        font = QtGui.QFont()
        font.setFamily("HanaMinA")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.enemy_choice_label.setFont(font)
        self.enemy_choice_label.setToolTip("")
        self.enemy_choice_label.setObjectName("enemy_choice_label")
        global enemy
        enemy = choice_enemy(0)
        self.enemy_choice_combobox_Layout.addWidget(self.enemy_choice_label)
        self.enemy_choice_combobox = QtWidgets.QComboBox(self.verticalLayoutWidget_11)
        self.enemy_choice_combobox.setObjectName("enemy_choice_combobox")
        self.enemy_choice_combobox.addItem("")
        self.enemy_choice_combobox.addItem("")
        self.enemy_choice_combobox.addItem("")
        self.enemy_choice_combobox.currentIndexChanged.connect(self.update_enemy)
        self.enemy_choice_combobox_Layout.addWidget(self.enemy_choice_combobox)
        self.enemy_info_text = QtWidgets.QTextEdit(self.main_frame)
        data = f"现实防御：{enemy.realistic_defense}\n精神防御：{enemy.mental_defense}\n受创减免：{round(enemy.injury_relief * 100, 2)}%\n暴击防御：{round(enemy.crit_defense * 100, 2)}%"
        self.enemy_info_text.setPlainText(data)
        self.enemy_info_text.setGeometry(QtCore.QRect(170, 300, 151, 76))
        self.enemy_info_text.setReadOnly(True)
        self.enemy_info_text.setObjectName("enemy_info_text")
        self.calculate_button = QtWidgets.QPushButton(self.main_frame)
        self.calculate_button.setGeometry(QtCore.QRect(360, 350, 151, 23))
        self.calculate_button.setObjectName("calculate_button")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.main_frame)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(360, 10, 160, 155))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")

        self.result_Layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.result_Layout.setContentsMargins(0, 0, 0, 0)
        self.result_Layout.setObjectName("result_Layout")
        self.result1_label = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.result1_label.setObjectName("result1_label")
        self.result_Layout.addWidget(self.result1_label)
        self.result1_output = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.result1_output.setText("")
        self.result1_output.setObjectName("result1_output")
        self.result_Layout.addWidget(self.result1_output)
        self.result2_label = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.result2_label.setObjectName("result2_label")
        self.result_Layout.addWidget(self.result2_label)
        self.result2_output = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.result2_output.setText("")
        self.result2_output.setObjectName("result2_output")
        self.result_Layout.addWidget(self.result2_output)
        self.result3_label = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.result3_label.setObjectName("result3_label")
        self.result_Layout.addWidget(self.result3_label)
        self.result3_output = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.result3_output.setText("")
        self.result3_output.setObjectName("result3_output")
        self.result_Layout.addWidget(self.result3_output)

        self.verticalLayout.addWidget(self.main_frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushbutton_close.clicked.connect(MainWindow.close)  # type: ignore
        self.pushbutton_max.toggled.connect(self.onButtonToggled)
        self.pushbutton_min.clicked.connect(MainWindow.showMinimized)  # type: ignore
        self.calculate_button.clicked.connect(self.calculate_damage)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.attack_label.setText(_translate("MainWindow", "面板攻击力："))
        self.critical_strike_rate_label.setText(_translate("MainWindow", "暴击率："))
        self.sign_3.setText(_translate("MainWindow", "%"))
        self.skill_ratio_laber.setText(_translate("MainWindow", "技能倍率："))
        self.sign_1.setText(_translate("MainWindow", "%"))
        self.critical_strike_ratio_label.setText(_translate("MainWindow", "暴击创伤："))
        self.sign_4.setText(_translate("MainWindow", "%"))
        self.damage_increase_label.setText(_translate("MainWindow", "伤害提升："))
        self.sign_2.setText(_translate("MainWindow", "%"))
        self.matchup_choice_label.setText(_translate("MainWindow", "属性克制："))
        self.matchup_choice_combobox.setItemText(0, _translate("MainWindow", "克制"))
        self.matchup_choice_combobox.setItemText(1, _translate("MainWindow", "非克制"))
        self.skill_choice_label.setText(_translate("MainWindow", "技能类型："))
        self.skill_choice_combobox.setItemText(0, _translate("MainWindow", "术法卡"))
        self.skill_choice_combobox.setItemText(1, _translate("MainWindow", "仪式卡"))
        self.damage_choice_label.setText(_translate("MainWindow", "伤害类型："))
        self.damage_choice_combobox.setItemText(0, _translate("MainWindow", "现实创伤"))
        self.damage_choice_combobox.setItemText(1, _translate("MainWindow", "精神创伤"))
        self.heart_choice_combobox_label.setText(_translate("MainWindow", "心相选择："))
        self.heart_choice_combobox.setItemText(0, _translate("MainWindow", "美丽新世界"))
        self.heart_choice_combobox.setItemText(1, _translate("MainWindow", "跳房子游戏"))
        self.heart_choice_combobox.setItemText(2, _translate("MainWindow", "第二次生命"))
        self.heart_choice_combobox.setItemText(3, _translate("MainWindow", "夜色亵渎者"))
        self.heart_choice_combobox.setItemText(4, _translate("MainWindow", "掌声如雷鸣"))
        self.heart_choice_combobox.setItemText(5, _translate("MainWindow", "好奇心宝贝"))
        self.heart_choice_combobox.setItemText(6, _translate("MainWindow", "大娱乐至上"))
        self.heart_choice_combobox.setItemText(7, _translate("MainWindow", "必要的记录"))
        self.heart_choice_combobox.setItemText(8, _translate("MainWindow", "在仙境之外"))
        self.heart_choice_combobox.setItemText(9, _translate("MainWindow", "可度量之心"))
        self.heart_info_text.setPlaceholderText(_translate("MainWindow", "请选择心相"))
        self.enemy_choice_label.setText(_translate("MainWindow", "敌人选择："))
        self.enemy_choice_combobox.setItemText(0, _translate("MainWindow", "凶兆·天蛾人"))
        self.enemy_choice_combobox.setItemText(1, _translate("MainWindow", "厄兆·天蛾人"))
        self.enemy_choice_combobox.setItemText(2, _translate("MainWindow", "无防御测试怪"))
        self.enemy_info_text.setPlaceholderText(_translate("MainWindow", "请选择敌人"))
        self.calculate_button.setText(_translate("MainWindow", "计算"))
        self.result1_label.setText(_translate("MainWindow", " 未暴击伤害："))
        self.result2_label.setText(_translate("MainWindow", " 暴击伤害："))
        self.result3_label.setText(_translate("MainWindow", " 暴击期望："))

    def onButtonToggled(self, checked):
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(':resources/images/max.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(':resources/images/return.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        if checked:
            self.pushbutton_max.setIcon(icon4)
        else:
            self.pushbutton_max.setIcon(icon1)

    def queryExit(self, MainWindow):

        MainWindow.close()

    def update_enemy(self, index):
        enemy = choice_enemy(index)

        if enemy:
            data = f"现实防御：{enemy.realistic_defense}\n精神防御：{enemy.mental_defense}\n受创减免：{round(enemy.injury_relief * 100, 2)}%\n暴击防御：{round(enemy.crit_defense * 100, 2)}%"
            self.enemy_info_text.setPlainText(data)

    def update_heart(self, index):
        heart = choice_heart(index)

        if heart:
            data = f"心相攻击力：{heart.heart_attack}\n仪式加成：{heart.ritual_power * 100}%\n术法加成：{heart.magic_power * 100}%\n创伤加成：{heart.damage_bonus * 100}%"
            self.heart_info_text.setPlainText(data)

    def calculate_damage(self):

        damage = self.damage_choice_combobox.currentIndex()

        if damage == 0:
            total_defense = enemy.realistic_defense
        elif damage == 1:
            total_defense = enemy.mental_defense

        match_up = self.matchup_choice_combobox.currentIndex()

        if match_up == 0:
            match_up_value = 0.3
        else:
            match_up_value = 0

        skill_choice = self.skill_choice_combobox.currentIndex()

        if skill_choice == 1:
            ritual_power = heart.ritual_power
            magic_power = 0
        else:
            ritual_power = 0
            magic_power = heart.magic_power

        total_attack = 0 if self.attack_input.text() == '' else float(self.attack_input.text())  # 面板攻击力（角色页面显示的攻击力）

        damage_increase = 0 if self.damage_increase_input.text() == '' else float(
            self.damage_increase_input.text()) / 100  # 伤害提升

        skill_ratio = 0 if self.skill_ratio_input.text() == '' else float(
            self.skill_ratio_input.text()) / 100  # 技能倍率

        critical_strike_rate = 0 if self.critical_strike_rate_input.text() == '' else float(
            self.critical_strike_rate_input.text()) / 100  # 暴击创伤

        critical_strike_ratio = 0 if self.critical_strike_ratio_input.text() == '' else float(
            self.critical_strike_ratio_input.text()) / 100  # 暴击率

        # 计算最终伤害
        regular_theoretical_damage = final_damage_calculation(total_attack, total_defense, heart.damage_bonus,
                                                              damage_increase, enemy.injury_relief,
                                                              skill_ratio, ritual_power, magic_power,
                                                              match_up_value)

        # 计算暴击伤害
        crit_damage = crit_damage_calculation(regular_theoretical_damage, critical_strike_ratio, enemy.crit_defense)

        # 计算暴击期望伤害
        critical_strike_expected_damage = critical_strike_expected_damage_calculation(regular_theoretical_damage,
                                                                                      critical_strike_rate,
                                                                                      critical_strike_ratio,
                                                                                      enemy.crit_defense)

        self.result1_output.setText(str(math.floor(regular_theoretical_damage)))
        self.result2_output.setText(str(math.floor(crit_damage)))
        self.result3_output.setText(str(math.floor(critical_strike_expected_damage)))
