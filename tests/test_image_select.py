import pytest
import os
import numpy as np
from PIL import Image as im

from src.crt import retro_filter
from tests.test_crt import is_similar
from src.__main__ import create_app

from PySide6.QtGui import QImage, QAction
from PySide6.QtWidgets import QApplication, QMenu
from PySide6.QtCore import Qt


@pytest.fixture
def app(qtbot):
    app, window = create_app(test_mode=True)
    qtbot.addWidget(window)
    return window


def qimage_to_array(image: QImage, channels: int = 3) -> np.ndarray:
    """Converts QImage to numpy array."""
    height, width = image.height(), image.width()
    image_bits = image.bits()
    image_array = np.array(image_bits).reshape(height, width, channels)
    return image_array


def test_crtify_button(app, qtbot):
    app.ui.path_to_file.setText(os.path.abspath(".\\tests\\test_images\\Eebee.jpg"))
    qtbot.mouseClick(app.ui.file_confirm, Qt.LeftButton)
    assert app.image is not None, "self.image was not set."


def test_crtify_custom_settings(app, qtbot):
    """tests similarity of image processed via the app with custom settings to that of an image processed by the function directly"""
    app.ui.path_to_file.setText(os.path.abspath(".\\tests\\test_images\\Eebee.jpg"))
    app.ui.input_curvature.setValue(5)
    qtbot.mouseClick(app.ui.custom_scan_lines, Qt.LeftButton)
    assert app.ui.custom_scan_lines.isChecked(), "Custom scan lines box did not check"
    app.ui.input_scan_lines.setValue(500)
    app.ui.input_vignette.setValue(20)
    qtbot.mouseClick(app.ui.file_confirm, Qt.LeftButton)
    app_result = qimage_to_array(app.image)
    function_result = retro_filter(
        ".\\tests\\test_images\\Eebee.jpg",
        curvature=5,
        scanline_val=500,
        vignette_width=20,
    )
    assert is_similar(function_result, app_result)


def test_save_button(app, qtbot):
    app.ui.path_to_file.setText(os.path.abspath(".\\tests\\test_images\\Eebee.jpg"))
    qtbot.mouseClick(app.ui.file_confirm, Qt.LeftButton)
    app.findChild(QAction, "save_image").trigger()
    app_result = qimage_to_array(app.image)
    saved_image = np.array(im.open(app.test_path))
    assert is_similar(app_result, saved_image, 0.94)
    os.remove(app.test_path)


def test_view_image(app, qtbot):  # TODO
    ...
