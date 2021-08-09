from PySide6 import QtWidgets
import pyautogui
import New_User
import Login_Class


class CreateWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.create_user_ui = New_User.Ui_NewUserWidget()
        self.create_user_ui.setupUi(self)
        self.screen_width, self.screen_height = pyautogui.size()
        self.window_pos_x = (self.screen_width - self.width()) / 2
        self.window_pos_y = (self.screen_height - self.height()) / 3
        self.move(self.window_pos_x, self.window_pos_y)

        self.create_user_ui.confirm_new_user_btnbx.accepted.connect(self.ok_button_clicked)
        self.create_user_ui.confirm_new_user_btnbx.rejected.connect(self.cancel_button_clicked)

    def ok_button_clicked(self):
        print("Hello")

    def cancel_button_clicked(self):
        self.close()
