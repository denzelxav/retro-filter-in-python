import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication

from src.image_select import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myApp = MainWindow()
    appIcon = QIcon()
    appIcon.addFile("..\\crt_icon.ico")
    myApp.setWindowIcon(appIcon)
    myApp.show()
    app.exec()
