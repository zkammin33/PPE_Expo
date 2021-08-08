from PySide6 import QtWidgets
import Login
import Main_Window_Class


class LogWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Login.Ui_Form()
        self.ui.setupUi(self)
        self.new_ui = Main_Window_Class.NewWindow()

        self.ui.log_button.clicked.connect(self.log_button_clicked)

    def log_button_clicked(self):
        #self.new_ui = Main_Window_Class.NewWindow()
        self.new_ui.show()
        self.close()
