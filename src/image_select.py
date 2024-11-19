import sys
import os
from PySide6 import QtWidgets
from PySide6.QtWidgets import QDialog, QApplication, QFileDialog
import matplotlib.pyplot as plt
from src.crt import *

from src.ui.output import Ui_Dialog


class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.browse_button.clicked.connect(self.browsefiles)
        self.ui.file_confirm.clicked.connect(self.crtify)

    def browsefiles(self):
        fname = QFileDialog.getOpenFileName(
            self,
            "Open file",
            f"C:\\Users\\{os.getlogin()}\\Downloads",
            "Image files (*.jpg *.jpeg *.png)",
        )
        self.ui.path_to_file.setText(fname[0])

    def crtify(self):
        file_path = self.ui.path_to_file.text()
        plt.imshow(retro_filter(file_path))
        plt.show()


app = QApplication(sys.argv)
mainwindow = MainWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(400)
widget.setFixedHeight(100)
widget.show()
sys.exit(app.exec())
