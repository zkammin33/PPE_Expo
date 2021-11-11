from PySide6 import QtWidgets
import Login
import Main_Window_Class
import New_User_Class
import mysql.connector
from mysql.connector import Error


class LogWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Login.Ui_Form()
        self.ui.setupUi(self)
        self.member_id = 0
        self.member_username = ""
        self.member_password = ""
        self.new_ui = Main_Window_Class.MainWindow()
        self.create_ui = None

        self.ui.log_button.clicked.connect(self.log_button_clicked)
        self.ui.create_button.clicked.connect(self.create_button_clicked)

    def log_button_clicked(self):
        if self.check_login_cred():
            self.member_username = self.ui.username_input.text()
            self.member_password = self.ui.pass_input.text()
            self.new_ui.set_member_info(self.member_id, self.member_username, self.member_password)
            self.new_ui.show()
            self.close()
        else:
            print("Email or Password incorrect")

    def create_button_clicked(self):
        self.create_ui = New_User_Class.CreateWindow()
        self.create_ui.show()

    # Need to check password from SQL database against the input
    def check_login_cred(self):
        try:
            cnx = mysql.connector.connect(host='localhost', user=self.ui.username_input.text(),
                                          password=self.ui.pass_input.text(), database="ZKammin")
            cursor = cnx.cursor()
            cursor.execute(f"SELECT id FROM user_info WHERE email = '{self.ui.username_input.text()}'")
            self.member_id = cursor.fetchone()[0]
            return True
        except Error as e:
            return False
