import sys
import os
from PySide6 import QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtWidgets import QDialog, QApplication, QFileDialog
import matplotlib.pyplot as plt
from src.crt import *
from PIL import Image as im

from src.ui.output import Ui_Dialog


class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.title = "CRTifier"
        self.ui.image_label.setPixmap
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

        im_np = retro_filter(file_path)
        im.fromarray(im_np, "RGB").show()
        print(im_np.shape)
        height, width, channels = im_np.shape
        bytes_per_line = width * channels
        image = QImage(im_np, width, height, bytes_per_line, QImage.Format_RGB888)

        self.ui.image_label.setScaledContents(True)
        self.ui.image_label.setPixmap(
            QPixmap(image).scaled(
                self.ui.image_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation
            )
        )
        self.ui.image_label.resize(im_np.shape[1], im_np.shape[0])


app = QApplication(sys.argv)
mainwindow = MainWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.resize(400, 300)
# widget.setFixedWidth(400)
# widget.setFixedHeight(500)
widget.show()
sys.exit(app.exec())
