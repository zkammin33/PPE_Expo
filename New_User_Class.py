import mysql.connector
from PySide6 import QtWidgets
import pyautogui
import New_User
import Login_Class
from mysql.connector import connect, Error


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
        self.create_user_ui.phone_num_input.textChanged.connect(self.on_text_change)
        self.create_user_ui.gender_input.textChanged.connect(self.on_text_change)
        self.create_user_ui.bday_month_input.textChanged.connect(self.on_text_change)
        self.create_user_ui.bday_day_input.textChanged.connect(self.on_text_change)
        self.create_user_ui.bday_year_input.textChanged.connect(self.on_text_change)

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

    # Inserting the new user information into the server
    def ok_button_clicked(self):
        try:
            cnx = mysql.connector.connect(host='localhost', user="LJKammin",
                                          password="Fire!4949", database="ZKammin")
            mycursor = cnx.cursor()
            mycursor.execute("""INSERT INTO user_info (first_name, middle_initial,
                             last_name, email, phone_number) VALUES
                             (%s,%s,%s,%s,%s)""",
                             (self.create_user_ui.first_name_input.text(),
                              self.create_user_ui.middle_name_input.text(),
                              self.create_user_ui.last_name_input.text(),
                              self.create_user_ui.new_email_input.text(),
                              self.create_user_ui.phone_num_input.text()))
            cnx.commit()

            # This needs to go in user settings or profile where gear will be scanned and added
            mycursor.execute(
                f"SELECT * FROM user_info WHERE first_name = '{self.create_user_ui.first_name_input.text()}'")
            row = mycursor.fetchall()
            member_id = row[0][0]
            mycursor.execute("INSERT INTO turnout_gear (owner_id, helmet_id, coat_id) VALUES "
                             "(%s,%s,%s)",
                             (member_id, 1112311, 123114))
            cnx.commit()
            cnx.close()
        except Error as e:
            print(e)

        self.close()

    # Exiting the new user window
    def cancel_button_clicked(self):
        self.close()

    # Making sure all of the text fields are filled before button is enabled
    def on_text_change(self):
        self.create_user_ui.create_button.setEnabled(bool(self.create_user_ui.first_name_input.text() and
                                                          self.create_user_ui.last_name_input.text() and
                                                          self.create_user_ui.middle_name_input.text() and
                                                          self.create_user_ui.bday_month_input.text() and
                                                          self.create_user_ui.bday_day_input.text() and
                                                          self.create_user_ui.bday_year_input.text() and
                                                          self.create_user_ui.gender_input.text() and
                                                          self.create_user_ui.new_email_input.text() and
                                                          self.create_user_ui.phone_num_input.text()))
