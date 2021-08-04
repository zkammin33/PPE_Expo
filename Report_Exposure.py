# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Report_Exposure.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1314, 887)
        Form.setAutoFillBackground(False)
        self.ButtonFrame = QFrame(Form)
        self.ButtonFrame.setObjectName(u"ButtonFrame")
        self.ButtonFrame.setGeometry(QRect(20, 70, 240, 431))
        self.ButtonFrame.setFrameShape(QFrame.WinPanel)
        self.ButtonFrame.setFrameShadow(QFrame.Plain)
        self.inventory_button = QPushButton(self.ButtonFrame)
        self.inventory_button.setObjectName(u"inventory_button")
        self.inventory_button.setGeometry(QRect(25, 160, 191, 111))
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.inventory_button.setFont(font)
        self.report_button = QPushButton(self.ButtonFrame)
        self.report_button.setObjectName(u"report_button")
        self.report_button.setGeometry(QRect(25, 20, 191, 111))
        self.report_button.setFont(font)
        self.genrep_button = QPushButton(self.ButtonFrame)
        self.genrep_button.setObjectName(u"genrep_button")
        self.genrep_button.setGeometry(QRect(25, 300, 191, 111))
        self.genrep_button.setFont(font)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 600, 240, 241))
        self.frame.setFrameShape(QFrame.Panel)
        self.frame.setFrameShadow(QFrame.Sunken)
        self.frame.setLineWidth(10)
        self.Logout_Button = QPushButton(self.frame)
        self.Logout_Button.setObjectName(u"Logout_Button")
        self.Logout_Button.setGeometry(QRect(25, 180, 191, 35))
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        self.Logout_Button.setFont(font1)
        self.Logout_Button.setAutoDefault(False)
        self.Logout_Button.setFlat(False)
        self.scan_button = QPushButton(self.frame)
        self.scan_button.setObjectName(u"scan_button")
        self.scan_button.setGeometry(QRect(25, 30, 191, 35))
        font2 = QFont()
        font2.setPointSize(18)
        font2.setBold(True)
        self.scan_button.setFont(font2)
        self.scan_button.setAutoDefault(False)
        self.scan_button.setFlat(False)
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(770, 440, 75, 24))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Main Screen", None))
        self.inventory_button.setText(QCoreApplication.translate("Form", u"Inventory", None))
        self.report_button.setText(QCoreApplication.translate("Form", u"Report\n"
"Exposure", None))
        self.genrep_button.setText(QCoreApplication.translate("Form", u"Generate \n"
"Report", None))
        self.Logout_Button.setText(QCoreApplication.translate("Form", u"Logout", None))
        self.scan_button.setText(QCoreApplication.translate("Form", u"Scan Gear", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"PushButton", None))
    # retranslateUi

