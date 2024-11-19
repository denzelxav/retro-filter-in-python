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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(369, 104)
        self.path_to_file = QLineEdit(Dialog)
        self.path_to_file.setObjectName(u"path_to_file")
        self.path_to_file.setGeometry(QRect(10, 30, 261, 21))
        self.browse_button = QPushButton(Dialog)
        self.browse_button.setObjectName(u"browse_button")
        self.browse_button.setGeometry(QRect(290, 30, 75, 24))
        self.file_confirm = QPushButton(Dialog)
        self.file_confirm.setObjectName(u"file_confirm")
        self.file_confirm.setGeometry(QRect(10, 60, 75, 24))
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 151, 16))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.browse_button.setText(QCoreApplication.translate("Dialog", u"Browse...", None))
        self.file_confirm.setText(QCoreApplication.translate("Dialog", u"CRTify!", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Select image to make retro!", None))
    # retranslateUi

