# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'New_User.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_NewUserWidget(object):
    def setupUi(self, NewUserWidget):
        if not NewUserWidget.objectName():
            NewUserWidget.setObjectName(u"NewUserWidget")
        NewUserWidget.resize(360, 706)
        NewUserWidget.setInputMethodHints(Qt.ImhNone)
        self.first_name_input = QLineEdit(NewUserWidget)
        self.first_name_input.setObjectName(u"first_name_input")
        self.first_name_input.setGeometry(QRect(20, 80, 321, 31))
        font = QFont()
        font.setPointSize(20)
        self.first_name_input.setFont(font)
        self.first_name_input.setTabletTracking(False)
        self.first_name_input.setFrame(True)
        self.first_name_input.setClearButtonEnabled(False)
        self.first_name_label = QLabel(NewUserWidget)
        self.first_name_label.setObjectName(u"first_name_label")
        self.first_name_label.setGeometry(QRect(20, 40, 171, 31))
        font1 = QFont()
        font1.setPointSize(24)
        font1.setBold(True)
        self.first_name_label.setFont(font1)
        self.first_name_label.setFocusPolicy(Qt.NoFocus)
        self.last_name_label = QLabel(NewUserWidget)
        self.last_name_label.setObjectName(u"last_name_label")
        self.last_name_label.setGeometry(QRect(20, 210, 171, 31))
        self.last_name_label.setFont(font1)
        self.last_name_input = QLineEdit(NewUserWidget)
        self.last_name_input.setObjectName(u"last_name_input")
        self.last_name_input.setGeometry(QRect(20, 250, 321, 31))
        self.last_name_input.setFont(font)
        self.new_email_label = QLabel(NewUserWidget)
        self.new_email_label.setObjectName(u"new_email_label")
        self.new_email_label.setGeometry(QRect(20, 460, 91, 31))
        self.new_email_label.setFont(font1)
        self.new_email_input = QLineEdit(NewUserWidget)
        self.new_email_input.setObjectName(u"new_email_input")
        self.new_email_input.setGeometry(QRect(20, 500, 321, 31))
        self.new_email_input.setFont(font)
        self.middle_name_label = QLabel(NewUserWidget)
        self.middle_name_label.setObjectName(u"middle_name_label")
        self.middle_name_label.setGeometry(QRect(20, 130, 211, 31))
        self.middle_name_label.setFont(font1)
        self.middle_name_input = QLineEdit(NewUserWidget)
        self.middle_name_input.setObjectName(u"middle_name_input")
        self.middle_name_input.setGeometry(QRect(20, 170, 321, 31))
        self.middle_name_input.setFont(font)
        self.phone_num_label = QLabel(NewUserWidget)
        self.phone_num_label.setObjectName(u"phone_num_label")
        self.phone_num_label.setGeometry(QRect(20, 550, 231, 31))
        self.phone_num_label.setFont(font1)
        self.phone_num_input = QLineEdit(NewUserWidget)
        self.phone_num_input.setObjectName(u"phone_num_input")
        self.phone_num_input.setGeometry(QRect(20, 590, 321, 31))
        self.phone_num_input.setFont(font)
        self.phone_num_input.setInputMethodHints(Qt.ImhDigitsOnly|Qt.ImhPreferNumbers)
        self.create_button = QPushButton(NewUserWidget)
        self.create_button.setObjectName(u"create_button")
        self.create_button.setEnabled(False)
        self.create_button.setGeometry(QRect(184, 663, 81, 25))
        font2 = QFont()
        font2.setPointSize(12)
        self.create_button.setFont(font2)
        self.cancel_button = QPushButton(NewUserWidget)
        self.cancel_button.setObjectName(u"cancel_button")
        self.cancel_button.setGeometry(QRect(270, 663, 81, 25))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(False)
        self.cancel_button.setFont(font3)
        self.gender_input = QLineEdit(NewUserWidget)
        self.gender_input.setObjectName(u"gender_input")
        self.gender_input.setGeometry(QRect(20, 410, 321, 31))
        self.gender_input.setFont(font)
        self.gende_label = QLabel(NewUserWidget)
        self.gende_label.setObjectName(u"gende_label")
        self.gende_label.setGeometry(QRect(20, 370, 111, 31))
        self.gende_label.setFont(font1)
        self.birth_date_label = QLabel(NewUserWidget)
        self.birth_date_label.setObjectName(u"birth_date_label")
        self.birth_date_label.setGeometry(QRect(20, 290, 351, 41))
        font4 = QFont()
        font4.setPointSize(20)
        font4.setBold(True)
        self.birth_date_label.setFont(font4)
        self.bday_month_input = QLineEdit(NewUserWidget)
        self.bday_month_input.setObjectName(u"bday_month_input")
        self.bday_month_input.setGeometry(QRect(20, 330, 71, 31))
        self.bday_month_input.setFont(font)
        self.bday_month_input.setMaxLength(2)
        self.bday_month_input.setAlignment(Qt.AlignCenter)
        self.bday_day_input = QLineEdit(NewUserWidget)
        self.bday_day_input.setObjectName(u"bday_day_input")
        self.bday_day_input.setGeometry(QRect(110, 330, 71, 31))
        self.bday_day_input.setFont(font)
        self.bday_day_input.setMaxLength(2)
        self.bday_day_input.setAlignment(Qt.AlignCenter)
        self.bday_year_input = QLineEdit(NewUserWidget)
        self.bday_year_input.setObjectName(u"bday_year_input")
        self.bday_year_input.setGeometry(QRect(200, 330, 141, 31))
        self.bday_year_input.setFont(font)
        self.bday_year_input.setMaxLength(4)
        self.bday_year_input.setFrame(True)
        self.bday_year_input.setAlignment(Qt.AlignCenter)
        self.first_name_input.raise_()
        self.first_name_label.raise_()
        self.last_name_label.raise_()
        self.last_name_input.raise_()
        self.new_email_label.raise_()
        self.new_email_input.raise_()
        self.middle_name_label.raise_()
        self.phone_num_label.raise_()
        self.phone_num_input.raise_()
        self.middle_name_input.raise_()
        self.create_button.raise_()
        self.cancel_button.raise_()
        self.gender_input.raise_()
        self.gende_label.raise_()
        self.birth_date_label.raise_()
        self.bday_month_input.raise_()
        self.bday_day_input.raise_()
        self.bday_year_input.raise_()
        QWidget.setTabOrder(self.first_name_input, self.middle_name_input)
        QWidget.setTabOrder(self.middle_name_input, self.last_name_input)
        QWidget.setTabOrder(self.last_name_input, self.bday_month_input)
        QWidget.setTabOrder(self.bday_month_input, self.bday_day_input)
        QWidget.setTabOrder(self.bday_day_input, self.bday_year_input)
        QWidget.setTabOrder(self.bday_year_input, self.gender_input)
        QWidget.setTabOrder(self.gender_input, self.new_email_input)
        QWidget.setTabOrder(self.new_email_input, self.phone_num_input)
        QWidget.setTabOrder(self.phone_num_input, self.create_button)
        QWidget.setTabOrder(self.create_button, self.cancel_button)

        self.retranslateUi(NewUserWidget)

        QMetaObject.connectSlotsByName(NewUserWidget)
    # setupUi

    def retranslateUi(self, NewUserWidget):
        NewUserWidget.setWindowTitle(QCoreApplication.translate("NewUserWidget", u"Create New User", None))
        self.first_name_label.setText(QCoreApplication.translate("NewUserWidget", u"First Name", None))
        self.last_name_label.setText(QCoreApplication.translate("NewUserWidget", u"Last Name", None))
        self.new_email_label.setText(QCoreApplication.translate("NewUserWidget", u"Email", None))
        self.middle_name_label.setText(QCoreApplication.translate("NewUserWidget", u"Middle Name", None))
        self.phone_num_label.setText(QCoreApplication.translate("NewUserWidget", u"Phone Number", None))
        self.create_button.setText(QCoreApplication.translate("NewUserWidget", u"Create", None))
        self.cancel_button.setText(QCoreApplication.translate("NewUserWidget", u"Cancel", None))
        self.gender_input.setText("")
        self.gende_label.setText(QCoreApplication.translate("NewUserWidget", u"Gender", None))
        self.birth_date_label.setText(QCoreApplication.translate("NewUserWidget", u"Birth Date (mm/dd/yyyy)", None))
        self.bday_month_input.setText("")
        self.bday_day_input.setText("")
        self.bday_year_input.setText("")
    # retranslateUi

