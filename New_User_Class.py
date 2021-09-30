import mysql.connector
from PySide6 import QtWidgets
import pyautogui
import New_User
from mysql.connector import connect, Error
from getpass import getpass


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

        # try:
        #     with connect(
        #         host="localhost",
        #         #user=input("Enter Username: "),
        #         #password=getpass("Enter Password: "),
        #         user="ZPKammin",
        #         password="Coebaseball1!",
        #         database="ZKammin"
        #     ) as connection:
        #         print(connection)
        #         with connection.cursor() as cursor:
        #             cursor.execute("DESCRIBE user_info")
        #             for x in cursor:
        #                 print(x)
        #         cursor.close()
        #         connection.close()
        # except Error as e:
        #     print(e)
        # print("DONE")


    def ok_button_clicked(self):
        try:
            cnx = mysql.connector.connect(host='localhost', user="ZPKammin",
                                          password="Coebaseball1!", database="ZKammin")
            mycursor = cnx.cursor()
            mycursor.execute("""INSERT INTO user_info (first_name, middle_initial,
                             last_name, email, phone_number, password) VALUES
                             (%s,%s,%s,%s,%s,%s)""",
                                (self.create_user_ui.first_name_input.text(),
                                 self.create_user_ui.middle_name_input.text(),
                                 self.create_user_ui.last_name_input.text(),
                                 self.create_user_ui.new_email_input.text(),
                                 self.create_user_ui.phone_num_input.text(),
                                 self.create_user_ui.new_pass_input.text()))
            cnx.commit()

            mycursor.execute(f"SELECT * FROM user_info WHERE first_name = '{self.create_user_ui.first_name_input.text()}'")
            row = mycursor.fetchall()
            member_id = row[0][0]
            mycursor.execute("INSERT INTO turnout_gear (Owner_ID, Helmet, Coat) VALUES "
                             "(%s,%s,%s)",
                             (17, 1112311, 123114))
            cnx.commit()
        except Error as e:
            print(e)


        cnx.close()
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
