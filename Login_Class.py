from PySide6 import QtWidgets
import Login
import Main_Window_Class
import New_User_Class



class LogWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Login.Ui_Form()
        self.ui.setupUi(self)
        self.new_ui = Main_Window_Class.MainWindow()
        self.create_ui = None

        self.ui.log_button.clicked.connect(self.log_button_clicked)
        self.ui.create_button.clicked.connect(self.create_button_clicked)

    def log_button_clicked(self):
        if self.check_login_cred():
            self.new_ui.show()
            self.close()
        else:
            print("Email or Password incorrect")

    def create_button_clicked(self):
        self.create_ui = New_User_Class.CreateWindow()
        self.create_ui.show()

    # Need to check password from SQL database against the input
    def check_login_cred(self):
        if self.ui.email_input.text() == "1111" and self.ui.pass_input.text() == "1111":
            return True
        else:
            return False
