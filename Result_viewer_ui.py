# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Result_viewer.ui'
##
## Created by: Qt User Interface Compiler version 5.15.8
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore


class Ui_Form__viewer(object):
    def setupUi(self, Form__viewer):
        if not Form__viewer.objectName():
            Form__viewer.setObjectName(u"Form__viewer")
        Form__viewer.resize(629, 768)
        self.textBrowser__viewer = QTextBrowser(Form__viewer)
        self.textBrowser__viewer.setObjectName(u"textBrowser__viewer")
        self.textBrowser__viewer.setGeometry(QRect(0, 0, 631, 721))
        self.buttonBox__close = QDialogButtonBox(Form__viewer)
        self.buttonBox__close.setObjectName(u"buttonBox__close")
        self.buttonBox__close.setGeometry(QRect(540, 733, 80, 24))
        self.buttonBox__close.setStandardButtons(QDialogButtonBox.Close)

        self.retranslateUi(Form__viewer)
        self.buttonBox__close.clicked.connect(Form__viewer.close)

        QMetaObject.connectSlotsByName(Form__viewer)
    # setupUi

    def retranslateUi(self, Form__viewer):
        Form__viewer.setWindowTitle(QCoreApplication.translate("Form__viewer", u"Result_viewer", None))
    # retranslateUi

