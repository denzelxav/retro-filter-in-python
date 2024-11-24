import sys
import os
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
        save_image = self.ui.image_label.context_menu.addAction("Save Image")

        save_image.triggered.connect(self.handle_save_image)

        self.setWindowIcon(QIcon("../../crt_icon.ico"))

    def browsefiles(self):
        """ " Opens file dialog for user to select file. Runs when clicking browse button."""
        fname = QFileDialog.getOpenFileName(
            self,
            "Open file",
            f"C:/Users/{os.getlogin()}/Downloads/",
            "Image files (*.jpg *.jpeg *.png)",
        )
        if fname[0]:
            self.ui.path_to_file.setText(fname[0])

    def crtify(self) -> None:
        """ "CRTifies selected image and sets it as self.image. Runs when clicking CRTify button."""
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
        window_width = (
            image_x + image_width
            if image_x + image_width > self.standard_width
            else self.standard_width
        )
        window_height = image_y + image_height
        new_size = QSize(window_width, window_height)
        self.setMinimumSize(new_size)

    def custom_scan_lines(self):
        self.ui.input_scan_lines.setEnabled(self.ui.custom_scan_lines.isChecked())

    def contextMenuEvent(self, event):
        if self.ui.image_label.underMouse() and self.image is not None:
            self.ui.image_label.context_menu.exec_(event.globalPos())

    def handle_save_image(self):
        """ "Opens file explorer to save image set to self.image. Runs when clicking save image in context menu."""
        fname = QFileDialog.getSaveFileName(
            self,
            "Save Image",
            f"C:/Users/{os.getlogin()}/Pictures/*.jpg",
            filter=".jpg(*.jpg);;.PNG(*.png)",
        )
        self.image.save(fname[0])
