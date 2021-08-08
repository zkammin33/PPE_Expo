from PySide6 import QtWidgets
import sys
import Login_Class


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = Login_Class.LogWidget()
    widget.show()

    sys.exit(app.exec())


