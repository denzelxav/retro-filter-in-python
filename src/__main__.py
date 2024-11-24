import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QWidget

from src.image_select import MainWindow


def create_app() -> tuple[QApplication, QWidget]:
    app = QApplication.instance() or QApplication(sys.argv)
    myApp = MainWindow()
    appIcon = QIcon()
    appIcon.addFile("..\\crt_icon.ico")
    myApp.setWindowIcon(appIcon)
    myApp.show()
    return app, myApp


if __name__ == "__main__":
    app, _ = create_app()
    sys.exit(app.exec())
