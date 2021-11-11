# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Login.ui'
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
        Form.setEnabled(True)
        Form.resize(1000, 800)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(1000, 800))
        Form.setMaximumSize(QSize(1000, 800))
        self.username_input = QLineEdit(Form)
        self.username_input.setObjectName(u"email_input")
        self.username_input.setEnabled(True)
        self.username_input.setGeometry(QRect(250, 200, 500, 50))
        self.username_input.setMaxLength(100)
        self.username_input.setFrame(True)
        self.email_label = QLabel(Form)
        self.email_label.setObjectName(u"email_label")
        self.email_label.setGeometry(QRect(250, 140, 111, 51))
        font = QFont()
        font.setFamilies([u"Arial Black"])
        font.setPointSize(28)
        font.setBold(True)
        self.email_label.setFont(font)
        self.email_label.setMargin(0)
        self.pass_label = QLabel(Form)
        self.pass_label.setObjectName(u"pass_label")
        self.pass_label.setGeometry(QRect(250, 340, 201, 51))
        self.pass_label.setFont(font)
        self.pass_label.setMargin(0)
        self.pass_input = QLineEdit(Form)
        self.pass_input.setObjectName(u"pass_input")
        self.pass_input.setEnabled(True)
        self.pass_input.setGeometry(QRect(250, 400, 500, 50))
        self.pass_input.setMaxLength(100)
        self.pass_input.setFrame(True)
        self.log_button = QPushButton(Form)
        self.log_button.setObjectName(u"log_button")
        self.log_button.setGeometry(QRect(128, 570, 221, 141))
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        self.log_button.setFont(font1)
        self.tools_frame = QFrame(Form)
        self.tools_frame.setObjectName(u"tools_frame")
        self.tools_frame.setGeometry(QRect(651, 570, 221, 141))
        self.tools_frame.setFrameShape(QFrame.Box)
        self.tools_frame.setFrameShadow(QFrame.Sunken)
        self.tools_frame.setLineWidth(5)
        self.create_button = QPushButton(self.tools_frame)
        self.create_button.setObjectName(u"create_button")
        self.create_button.setGeometry(QRect(20, 20, 181, 41))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.create_button.setFont(font2)
        self.forgot_button = QPushButton(self.tools_frame)
        self.forgot_button.setObjectName(u"forgot_button")
        self.forgot_button.setGeometry(QRect(20, 80, 181, 41))
        self.forgot_button.setFont(font2)

        self.retranslateUi(Form)

        self.log_button.setDefault(True)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Login", None))
        self.email_label.setText(QCoreApplication.translate("Form", u"Email", None))
        self.pass_label.setText(QCoreApplication.translate("Form", u"Password", None))
        self.log_button.setText(QCoreApplication.translate("Form", u"Login", None))
        self.create_button.setText(QCoreApplication.translate("Form", u"Create New User", None))
        self.forgot_button.setText(QCoreApplication.translate("Form", u"Forgot Password", None))
    # retranslateUi

