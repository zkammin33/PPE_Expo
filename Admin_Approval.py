# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Admin_Approval.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_AdminApproveWidget(object):
    def setupUi(self, AdminApproveWidget):
        if not AdminApproveWidget.objectName():
            AdminApproveWidget.setObjectName(u"AdminApproveWidget")
        AdminApproveWidget.resize(300, 300)
        self.admin_un_input = QLineEdit(AdminApproveWidget)
        self.admin_un_input.setObjectName(u"admin_un_input")
        self.admin_un_input.setGeometry(QRect(25, 60, 250, 30))
        font = QFont()
        font.setPointSize(20)
        self.admin_un_input.setFont(font)
        self.admin_un_input.setEchoMode(QLineEdit.Normal)
        self.admin_pass_input = QLineEdit(AdminApproveWidget)
        self.admin_pass_input.setObjectName(u"admin_pass_input")
        self.admin_pass_input.setGeometry(QRect(25, 150, 250, 30))
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        self.admin_pass_input.setFont(font1)
        self.admin_pass_input.setEchoMode(QLineEdit.Password)
        self.admin_un_label = QLabel(AdminApproveWidget)
        self.admin_un_label.setObjectName(u"admin_un_label")
        self.admin_un_label.setGeometry(QRect(70, 20, 150, 40))
        font2 = QFont()
        font2.setPointSize(24)
        font2.setBold(True)
        self.admin_un_label.setFont(font2)
        self.admin_un_label.setAlignment(Qt.AlignCenter)
        self.admin_un_label_2 = QLabel(AdminApproveWidget)
        self.admin_un_label_2.setObjectName(u"admin_un_label_2")
        self.admin_un_label_2.setGeometry(QRect(70, 110, 150, 40))
        self.admin_un_label_2.setFont(font2)
        self.admin_un_label_2.setAlignment(Qt.AlignCenter)
        self.Inc_cred_label = QLabel(AdminApproveWidget)
        self.Inc_cred_label.setObjectName(u"Inc_cred_label")
        self.Inc_cred_label.setEnabled(True)
        self.Inc_cred_label.setGeometry(QRect(0, 200, 300, 20))
        font3 = QFont()
        font3.setPointSize(13)
        self.Inc_cred_label.setFont(font3)
        self.Inc_cred_label.setLayoutDirection(Qt.LeftToRight)
        self.Inc_cred_label.setAlignment(Qt.AlignCenter)
        self.create_button = QPushButton(AdminApproveWidget)
        self.create_button.setObjectName(u"create_button")
        self.create_button.setEnabled(False)
        self.create_button.setGeometry(QRect(60, 260, 81, 25))
        font4 = QFont()
        font4.setPointSize(12)
        self.create_button.setFont(font4)
        self.cancel_button = QPushButton(AdminApproveWidget)
        self.cancel_button.setObjectName(u"cancel_button")
        self.cancel_button.setGeometry(QRect(160, 260, 81, 25))
        font5 = QFont()
        font5.setPointSize(12)
        font5.setBold(False)
        self.cancel_button.setFont(font5)

        self.retranslateUi(AdminApproveWidget)

        QMetaObject.connectSlotsByName(AdminApproveWidget)
    # setupUi

    def retranslateUi(self, AdminApproveWidget):
        AdminApproveWidget.setWindowTitle(QCoreApplication.translate("AdminApproveWidget", u"Administration Approval", None))
        self.admin_un_label.setText(QCoreApplication.translate("AdminApproveWidget", u"Username", None))
        self.admin_un_label_2.setText(QCoreApplication.translate("AdminApproveWidget", u"Password", None))
        self.Inc_cred_label.setText(QCoreApplication.translate("AdminApproveWidget", u"Incorrect Credentials", None))
        self.create_button.setText(QCoreApplication.translate("AdminApproveWidget", u"Create", None))
        self.cancel_button.setText(QCoreApplication.translate("AdminApproveWidget", u"Cancel", None))
    # retranslateUi

