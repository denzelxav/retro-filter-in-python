# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'image_selector.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QDialog,
    QDoubleSpinBox, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpinBox, QWidget)

class Ui_ImageSelector(object):
    def setupUi(self, ImageSelector):
        if not ImageSelector.objectName():
            ImageSelector.setObjectName(u"ImageSelector")
        ImageSelector.setEnabled(True)
        ImageSelector.resize(372, 343)
        ImageSelector.setMinimumSize(QSize(372, 343))
        icon = QIcon()
        icon.addFile(u"../../crt_icon.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        ImageSelector.setWindowIcon(icon)
        self.path_to_file = QLineEdit(ImageSelector)
        self.path_to_file.setObjectName(u"path_to_file")
        self.path_to_file.setGeometry(QRect(10, 30, 261, 21))
        self.browse_button = QPushButton(ImageSelector)
        self.browse_button.setObjectName(u"browse_button")
        self.browse_button.setGeometry(QRect(290, 30, 75, 24))
        self.file_confirm = QPushButton(ImageSelector)
        self.file_confirm.setObjectName(u"file_confirm")
        self.file_confirm.setGeometry(QRect(10, 60, 75, 24))
        self.image_select_label = QLabel(ImageSelector)
        self.image_select_label.setObjectName(u"image_select_label")
        self.image_select_label.setGeometry(QRect(10, 10, 151, 16))
        self.image_label = QLabel(ImageSelector)
        self.image_label.setObjectName(u"image_label")
        self.image_label.setGeometry(QRect(10, 190, 211, 141))
        self.input_curvature = QDoubleSpinBox(ImageSelector)
        self.input_curvature.setObjectName(u"input_curvature")
        self.input_curvature.setGeometry(QRect(70, 90, 41, 22))
        self.input_curvature.setMinimum(-10.000000000000000)
        self.input_curvature.setMaximum(9999.989999999999782)
        self.input_curvature.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.input_curvature.setValue(2.000000000000000)
        self.input_scan_lines = QSpinBox(ImageSelector)
        self.input_scan_lines.setObjectName(u"input_scan_lines")
        self.input_scan_lines.setEnabled(False)
        self.input_scan_lines.setGeometry(QRect(140, 120, 42, 22))
        self.input_scan_lines.setMaximum(9999)
        self.input_vignette = QSpinBox(ImageSelector)
        self.input_vignette.setObjectName(u"input_vignette")
        self.input_vignette.setGeometry(QRect(60, 160, 42, 22))
        self.input_vignette.setMaximum(9999)
        self.input_vignette.setValue(10)
        self.curvature_label = QLabel(ImageSelector)
        self.curvature_label.setObjectName(u"curvature_label")
        self.curvature_label.setGeometry(QRect(10, 90, 61, 16))
        self.vignette_label = QLabel(ImageSelector)
        self.vignette_label.setObjectName(u"vignette_label")
        self.vignette_label.setGeometry(QRect(10, 160, 49, 16))
        self.custom_scan_lines = QCheckBox(ImageSelector)
        self.custom_scan_lines.setObjectName(u"custom_scan_lines")
        self.custom_scan_lines.setEnabled(True)
        self.custom_scan_lines.setGeometry(QRect(10, 120, 121, 20))
        self.custom_scan_lines.setChecked(False)

        self.retranslateUi(ImageSelector)

        QMetaObject.connectSlotsByName(ImageSelector)
    # setupUi

    def retranslateUi(self, ImageSelector):
        ImageSelector.setWindowTitle(QCoreApplication.translate("ImageSelector", u"CRTifier", None))
        self.path_to_file.setText("")
        self.browse_button.setText(QCoreApplication.translate("ImageSelector", u"Browse...", None))
        self.file_confirm.setText(QCoreApplication.translate("ImageSelector", u"CRTify!", None))
        self.image_select_label.setText(QCoreApplication.translate("ImageSelector", u"Select image to make retro!", None))
        self.image_label.setText(QCoreApplication.translate("ImageSelector", u"No image CRTified yet.", None))
#if QT_CONFIG(tooltip)
        self.input_curvature.setToolTip(QCoreApplication.translate("ImageSelector", u"<html><head/><body><p>The amount that the screen is curved.<br/>A lower value results in higer curvature.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.input_vignette.setToolTip(QCoreApplication.translate("ImageSelector", u"<html><head/><body><p>The amount of pixels from the border that the vignette will reach.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.curvature_label.setText(QCoreApplication.translate("ImageSelector", u"Curvature", None))
        self.vignette_label.setText(QCoreApplication.translate("ImageSelector", u"Vignette", None))
#if QT_CONFIG(tooltip)
        self.custom_scan_lines.setToolTip(QCoreApplication.translate("ImageSelector", u"<html><head/><body><p>Use custom scan line periodicity.<br/>When not selected, the scanlines alternate every pixel, like a real CRT.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.custom_scan_lines.setText(QCoreApplication.translate("ImageSelector", u"Custom Scan Lines", None))
    # retranslateUi

