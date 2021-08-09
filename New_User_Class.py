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

        self.create_user_ui.create_button.clicked.connect(self.ok_button_clicked)
        self.create_user_ui.cancel_button.clicked.connect(self.cancel_button_clicked)
        self.create_user_ui.first_name_input.textChanged.connect(self.on_text_change)
        self.create_user_ui.last_name_input.textChanged.connect(self.on_text_change)
        self.create_user_ui.middle_name_input.textChanged.connect(self.on_text_change)
        self.create_user_ui.new_email_input.textChanged.connect(self.on_text_change)
        self.create_user_ui.new_pass_input.textChanged.connect(self.on_text_change)
        self.create_user_ui.confirm_pass_input.textChanged.connect(self.on_text_change)
        self.create_user_ui.phone_num_input.textChanged.connect(self.on_text_change)

    def ok_button_clicked(self):
        print(self.create_user_ui.first_name_input.text())
        print(self.create_user_ui.last_name_input.text())
        print(self.create_user_ui.middle_name_input.text())
        print(self.create_user_ui.new_email_input.text())
        print(self.create_user_ui.new_pass_input.text())
        print(self.create_user_ui.confirm_pass_input.text())
        print(self.create_user_ui.phone_num_input.text())
        self.close()

    def cancel_button_clicked(self):
        self.close()

    def on_text_change(self):
        if (self.create_user_ui.first_name_input.text() != "" and
                self.create_user_ui.last_name_input.text() != "" and
                self.create_user_ui.middle_name_input.text() != "" and
                self.create_user_ui.new_email_input.text() != "" and
                self.create_user_ui.new_pass_input.text() != "" and
                self.create_user_ui.confirm_pass_input.text() != "" and
                self.create_user_ui.phone_num_input.text() != ""):

            self.create_user_ui.create_button.setEnabled(True)

        else:
            self.create_user_ui.create_button.setEnabled(False)
