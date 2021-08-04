from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice
from pyzbar import pyzbar
import cv2
import random
import sys
import pyautogui
import Login
import Main_Screen
import Report_Exposure

class LogWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Login.Ui_Form()
        self.ui.setupUi(self)

        self.ui.log_button.clicked.connect(self.log_button_clicked)

    def log_button_clicked(self):
        self.new_ui = NewWindow()
        self.new_ui.show()
        self.close()




class NewWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.log_ui = Main_Screen.Ui_Form()
        self.log_ui.setupUi(self)
        self.screen_width, self.screen_height = pyautogui.size()
        print(self.screen_width, self.screen_height)
        self.window_pos_x = (self.screen_width - self.width()) / 2
        self.window_pos_y = (self.screen_height - self.height()) / 3
        self.move(self.window_pos_x, self.window_pos_y)
        print(self.window_pos_x, self.window_pos_y)
        self.log_ui.main_widget.setCurrentWidget(self.log_ui.page_2)
        self.log_ui.expo_type_widget.setCurrentWidget(self.log_ui.inner_blank_page)
        self.log_ui.bio_chem_widget.setCurrentWidget(self.log_ui.expo_type_blank_page)

        self.bar_code_num = ""
        self.barcodes = None

        self.log_ui.Logout_Button.clicked.connect(self.on_log_button_clicked)
        self.log_ui.scan_button.clicked.connect(self.on_scan_button_clicked)
        self.log_ui.report_button.clicked.connect(self.on_report_button_clicked)
        self.log_ui.inventory_button.clicked.connect(self.on_inventory_button_clicked)
        self.log_ui.mats_search_btn.clicked.connect(self.on_mats_search_clicked)
        self.log_ui.expo_type_cmb.currentTextChanged.connect(self.on_exposure_change)
        self.log_ui.bio_radio_btn.toggled.connect(self.on_bio_expo_changed)
        self.log_ui.chem_radio_btn.toggled.connect(self.on_chem_expo_changed)


    def on_log_button_clicked(self):
        self.ui = LogWidget()
        self.ui.show()
        self.close()

    def on_scan_button_clicked(self):
        self.bar_code_num = ""
        self.run_barcode_reader()

    def on_report_button_clicked(self):
        self.log_ui.main_widget.setCurrentWidget(self.log_ui.report_expo_page)

    def on_inventory_button_clicked(self):
        self.log_ui.main_widget.setCurrentWidget(self.log_ui.page_2)

    def on_mats_search_clicked(self):
        un_file = open("UN_Nums.txt", "r")
        self.log_ui.mats_lists_widget.clear()

        searched_mat_upper = self.log_ui.mats_line_edit.text().title()
        searched_mat_lower = self.log_ui.mats_line_edit.text().lower()
        for line in un_file:
            if searched_mat_upper in line or searched_mat_lower in line:
                self.log_ui.mats_lists_widget.addItem(line)
        if self.log_ui.mats_lists_widget.count() == 0:
            self.log_ui.mats_lists_widget.addItem("No Materials Found")

        un_file.close()

    def on_exposure_change(self):
        if self.log_ui.expo_type_cmb.currentText() == "Fire":
            self.log_ui.expo_type_widget.setCurrentWidget(self.log_ui.expo_fire_page)
            #self.log_ui.stackedWidget_2.setGeometry(QtCore.QRect(410, 210, 581, 211))

        elif self.log_ui.expo_type_cmb.currentText() == "EMS":
            self.log_ui.expo_type_widget.setCurrentWidget(self.log_ui.expo_ems_page)
            #self.log_ui.stackedWidget_2.setGeometry(QtCore.QRect(410, 210, 581, 300))

        elif self.log_ui.expo_type_cmb.currentText() == "Hazmat":
            self.log_ui.expo_type_widget.setCurrentWidget(self.log_ui.expo_haz_page)

    def on_bio_expo_changed(self):
        if self.log_ui.bio_radio_btn.isChecked():
            self.log_ui.bio_chem_widget.setCurrentWidget(self.log_ui.bio_page)
            self.log_ui.chem_radio_btn.setChecked(False)

    def on_chem_expo_changed(self):
        if self.log_ui.chem_radio_btn.isChecked():
            self.log_ui.bio_chem_widget.setCurrentWidget(self.log_ui.chem_page)
            self.log_ui.bio_radio_btn.setChecked(False)


    def read_barcode(self, frame):
        self.barcodes = pyzbar.decode(frame)
        for barcode in self.barcodes:
            x, y, w, h = barcode.rect

            barcode_info = barcode.data.decode('utf-8')
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, barcode_info, (x + 6, y - 6), font, 2.0, (255, 255, 255), 1)

            self.bar_code_num = barcode_info

        return frame

    def run_barcode_reader(self):

        camera = cv2.VideoCapture(0)
        ret, frame = camera.read()

        while ret and self.bar_code_num == "":
            if self.bar_code_num != "":
                print(self.bar_code_num)
            ret, frame = camera.read()
            frame = self.read_barcode(frame)
            cv2.imshow('Barcode/QR code reader', frame)
            if cv2.waitKey(1) & 0xFF == 27:
                break

        camera.release()
        cv2.destroyAllWindows()

        print(f"Barcode number: {self.bar_code_num}")


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = LogWidget()
    widget.show()


    sys.exit(app.exec())


