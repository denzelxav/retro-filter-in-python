import subprocess
import sys
import os
import tempfile

from PySide6 import QtWidgets
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QPixmap, QImage, QIcon
from PySide6.QtWidgets import QDialog, QApplication, QFileDialog, QMenu
from numpy import ndarray
from src.crt import *
from src.ui.output import Ui_ImageSelector


class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_ImageSelector()
        self.ui.setupUi(self)
        self.image = None
        self.ui.path_to_file.setText(f"C:/Users/{os.getlogin()}/Downloads/")
        self.standard_width = self.width()

        # buttons
        self.setWindowFlag(Qt.WindowType.WindowMinimizeButtonHint)
        self.setWindowFlag(Qt.WindowType.WindowMaximizeButtonHint)
        self.ui.browse_button.clicked.connect(self.browsefiles)
        self.ui.file_confirm.clicked.connect(self.crtify)
        self.ui.custom_scan_lines.stateChanged.connect(self.custom_scan_lines)

        # context menu
        self.ui.image_label.context_menu = QMenu(self)
        open_in_viewer = self.ui.image_label.context_menu.addAction(
            "Open Image in Viewer"
        )
        save_image = self.ui.image_label.context_menu.addAction("Save Image")

        open_in_viewer.triggered.connect(self.open_image)
        save_image.triggered.connect(self.handle_save_image)

        self.setWindowIcon(QIcon("../../crt_icon.ico"))

    def custom_scan_lines(self):
        self.ui.input_scan_lines.setEnabled(self.ui.custom_scan_lines.isChecked())

    def contextMenuEvent(self, event):
        if self.ui.image_label.underMouse() and self.image is not None:
            self.ui.image_label.context_menu.exec_(event.globalPos())

    def open_image(self):
        image_path = self.image_temp_file()
        if sys.platform == "win32":
            os.startfile(image_path)
        elif sys.platform == "darwin":
            os.system(f'open "{image_path}"')
        else:  # Assuming a Linux-based system
            os.system(f'xdg-open "{image_path}"')

    def handle_save_image(self):
        fname = QFileDialog.getSaveFileName(
            self,
            "Save Image",
            f"C:/Users/{os.getlogin()}/Pictures/*.jpg",
            filter=".jpg(*.jpg);;.PNG(*.png)",
        )
        print(self.image.save(fname[0]))

    def browsefiles(self):
        fname = QFileDialog.getOpenFileName(
            self,
            "Open file",
            f"C:/Users/{os.getlogin()}/Downloads/",
            "Image files (*.jpg *.jpeg *.png)",
        )
        if fname[0]:
            self.ui.path_to_file.setText(fname[0])

    def crtify(self):
        file_path = self.ui.path_to_file.text()

        curvature = self.ui.input_curvature.value()
        scan_line_val = (
            self.ui.input_scan_lines.value()
            if self.ui.custom_scan_lines.isChecked()
            else None
        )
        vignette_width = self.ui.input_vignette.value()

        try:
            image_array: ndarray[int | ndarray[int]] = retro_filter(
                file_path,
                curvature=curvature,
                scanline_val=scan_line_val,
                vignette_width=vignette_width,
            )
        except PermissionError:
            self.ui.image_label.setText("Error: permission denied")
        except FileNotFoundError:
            self.ui.image_label.setText("Error: file not found")
        image_height, image_width, image_channels = image_array.shape
        bytes_per_line = image_width * image_channels

        self.image = QImage(
            image_array, image_width, image_height, bytes_per_line, QImage.Format_RGB888
        )

        self.ui.image_label.setScaledContents(True)
        self.ui.image_label.setPixmap(
            QPixmap(self.image).scaled(
                self.ui.image_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation
            )
        )
        self.ui.image_label.resize(image_width, image_height)
        self.resize_for_image()

    def resize_for_image(self) -> None:
        """Adjusts the minimum window size to make the picture fit"""
        image_x, image_y = self.ui.image_label.x(), self.ui.image_label.y()
        image_width, image_height = (
            self.ui.image_label.width(),
            self.ui.image_label.height(),
        )
        print(self.size())
        window_width = (
            image_x + image_width
            if image_x + image_width > self.standard_width
            else self.standard_width
        )
        window_height = image_y + image_height
        new_size = QSize(window_width, window_height)
        print(new_size)
        self.setMinimumSize(new_size)

    def image_temp_file(self, format=".jpg"):
        temp_file = tempfile.NamedTemporaryFile(
            delete=False, suffix=f"{format.lower()}"
        )
        temp_file.close()
        self.image.save(temp_file.name, quality=100)
        return temp_file.name
