from PySide6 import QtWidgets
import pyautogui
from pyzbar import pyzbar
import cv2
import Main_Screen
import Login_Class


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.main_win_ui = Main_Screen.Ui_Form()
        self.main_win_ui.setupUi(self)
        self.screen_width, self.screen_height = pyautogui.size()
        self.window_pos_x = (self.screen_width - self.width()) / 2
        self.window_pos_y = (self.screen_height - self.height()) / 3
        self.move(self.window_pos_x, self.window_pos_y)
        self.main_win_ui.main_widget.setCurrentWidget(self.main_win_ui.page_2)
        self.main_win_ui.expo_type_widget.setCurrentWidget(self.main_win_ui.inner_blank_page)
        self.main_win_ui.bio_chem_widget.setCurrentWidget(self.main_win_ui.expo_type_blank_page)

        self.bar_code_num = ""
        self.barcodes = None

        self.main_win_ui.Logout_Button.clicked.connect(self.on_log_button_clicked)
        self.main_win_ui.scan_button.clicked.connect(self.on_scan_button_clicked)
        self.main_win_ui.report_button.clicked.connect(self.on_report_button_clicked)
        self.main_win_ui.inventory_button.clicked.connect(self.on_inventory_button_clicked)
        self.main_win_ui.mats_search_btn.clicked.connect(self.on_mats_search_clicked)
        self.main_win_ui.expo_type_cmb.currentTextChanged.connect(self.on_exposure_change)
        self.main_win_ui.bio_radio_btn.toggled.connect(self.on_bio_expo_changed)
        self.main_win_ui.chem_radio_btn.toggled.connect(self.on_chem_expo_changed)

    def on_log_button_clicked(self):
        self.ui = Login_Class.LogWidget()
        self.ui.show()
        self.close()

    def on_scan_button_clicked(self):
        self.bar_code_num = ""
        self.run_barcode_reader()

    def on_report_button_clicked(self):
        self.main_win_ui.main_widget.setCurrentWidget(self.main_win_ui.report_expo_page)

    def on_inventory_button_clicked(self):
        self.main_win_ui.main_widget.setCurrentWidget(self.main_win_ui.page_2)

    def on_mats_search_clicked(self):
        un_file = open("UN_Nums.txt", "r")
        self.main_win_ui.mats_lists_widget.clear()

        searched_mat_upper = self.main_win_ui.mats_line_edit.text().title().lower()
        #searched_mat_lower = self.main_win_ui.mats_line_edit.text().lower()
        for line in un_file:
            if searched_mat_upper in line or searched_mat_upper in line:
                self.main_win_ui.mats_lists_widget.addItem(line)
        if self.main_win_ui.mats_lists_widget.count() == 0:
            self.main_win_ui.mats_lists_widget.addItem("No Materials Found")

        un_file.close()

    def on_exposure_change(self):
        if self.main_win_ui.expo_type_cmb.currentText() == "Fire":
            self.main_win_ui.expo_type_widget.setCurrentWidget(self.main_win_ui.expo_fire_page)

        elif self.main_win_ui.expo_type_cmb.currentText() == "EMS":
            self.main_win_ui.expo_type_widget.setCurrentWidget(self.main_win_ui.expo_ems_page)

        elif self.main_win_ui.expo_type_cmb.currentText() == "Hazmat":
            self.main_win_ui.expo_type_widget.setCurrentWidget(self.main_win_ui.expo_haz_page)

        elif self.main_win_ui.expo_type_cmb.currentText() == "Technical Rescue":
            self.main_win_ui.expo_type_widget.setCurrentWidget(self.main_win_ui.expo_tech_page)

    def on_bio_expo_changed(self):
        if self.main_win_ui.bio_radio_btn.isChecked():
            self.main_win_ui.bio_chem_widget.setCurrentWidget(self.main_win_ui.bio_page)
            self.main_win_ui.chem_radio_btn.setChecked(False)

    def on_chem_expo_changed(self):
        if self.main_win_ui.chem_radio_btn.isChecked():
            self.main_win_ui.bio_chem_widget.setCurrentWidget(self.main_win_ui.chem_page)
            self.main_win_ui.bio_radio_btn.setChecked(False)


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