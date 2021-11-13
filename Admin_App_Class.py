from PySide6 import QtWidgets
import pyautogui
import mysql.connector
from mysql.connector import Error, errorcode
import Admin_Approval


class AdminAppWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.admin_win_ui = Admin_Approval.Ui_AdminApproveWidget()
        self.admin_win_ui.setupUi(self)
        self.screen_width, self.screen_height = pyautogui.size()
        self.window_pos_x = (self.screen_width - self.width()) / 2
        self.window_pos_y = (self.screen_height - self.height()) / 3
        self.move(self.window_pos_x, self.window_pos_y)

        self.admin_win_ui.Inc_cred_label.hide()

        self.admin_win_ui.create_button.clicked.connect(self.create_button_clicked)
        self.admin_win_ui.cancel_button.clicked.connect(self.cancel_button_clicked)
        self.admin_win_ui.admin_un_input.textChanged.connect(self.on_text_change)
        self.admin_win_ui.admin_pass_input.textChanged.connect(self.on_text_change)
        self.admin_win_ui.admin_un_input.textChanged.connect(self.clear_cred_label_un)
        self.admin_win_ui.admin_pass_input.textChanged.connect(self.clear_cred_label_pass)

    def create_button_clicked(self):
        self.admin_win_ui.Inc_cred_label.hide()
        if self.check_login_cred():
            print("Login Success")
        else:
            self.admin_win_ui.Inc_cred_label.show()
            self.admin_win_ui.admin_un_input.clear()
            self.admin_win_ui.admin_pass_input.clear()

    def cancel_button_clicked(self):
        self.close()

    def check_login_cred(self):
        try:
            cnx = mysql.connector.connect(host='localhost', user=self.admin_win_ui.admin_un_input.text(),
                                          password=self.admin_win_ui.admin_pass_input.text(), database="ZKammin")

            # NEED TO: Create the user based on the information given
            cursor = cnx.cursor()
            cursor.execute(f"SELECT id FROM user_info WHERE email = '{self.admin_win_ui.admin_un_input.text()}'")
            return True
        except Error as e:
            # Error Code 1045
            if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                self.admin_win_ui.Inc_cred_label.setText("Incorrect Credentials")
            # Error Code 1162
            elif e.errno == errorcode.ER_TABLEACCESS_DENIED_ERROR:
                self.admin_win_ui.Inc_cred_label.setText("Access Denied")
            return False

    # Determining if create button should be enable to disabled based on the input fields
    def on_text_change(self):
        self.admin_win_ui.create_button.setEnabled(bool(self.admin_win_ui.admin_un_input.text() and
                                                        self.admin_win_ui.admin_pass_input.text()))

    # Clearing the incorrect credentials label when re-entering in the username
    def clear_cred_label_un(self):
        if self.admin_win_ui.Inc_cred_label.isVisible() and self.admin_win_ui.admin_un_input.text() != "":
            self.admin_win_ui.Inc_cred_label.hide()

    # Clearing the incorrect credentials lable when re-entering the password
    def clear_cred_label_pass(self):
        if self.admin_win_ui.Inc_cred_label.isVisible() and self.admin_win_ui.admin_pass_input.text() != "":
            self.admin_win_ui.Inc_cred_label.hide()
