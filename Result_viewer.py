import pathlib
from PySide2 import QtWidgets, QtGui, QtCore

import Result_viewer_ui
import importlib

importlib.reload(Result_viewer_ui)


class Viewer(QtWidgets.QWidget, Result_viewer_ui.Ui_Form__viewer):
    def __init__(self, parent=None):
        super(Viewer, self).__init__(parent)

        self.setupUi(self)

    @property
    def main(self):
        return self.__main

    def read_file(self, r_path: pathlib.Path):
        if r_path.is_dir():
            return
        source = []
        with open(r_path, 'rt') as rl:
            source += rl.readlines()
            result = ''.join(source)
        self.textBrowser__viewer.setPlainText(str(result))