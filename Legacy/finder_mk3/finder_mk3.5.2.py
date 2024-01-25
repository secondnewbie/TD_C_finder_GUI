#!/usr/bin/python3
#encoding=utf-8
import sys
import pathlib
import re
from PySide2 import QtWidgets, QtGui, QtCore
import Finder_mk3_ui
import importlib

importlib.reload(Finder_mk3_ui)

class Name:
    class Keyword:
        keyword = 'name_keyword'

    class Path:
        tar_path = 'name_tar_path'
        save_path = 'name_save_path'

    class Result:
        result = 'name_result'

class GUI(QtWidgets.QWidget, Finder_mk3_ui.Ui_Form):
    def __init__(self, parent=None):
        super(GUI, self).__init__(parent)

        self.setupUi(self)

        self._signal_func()

    def _signal_func(self):
        self.buttonBox__targetpath.clicked.connect(self.slot_open)
        self.buttonBox__save.clicked.connect(self.slot_save)
        self.buttonBox__ok.clicked.connect(self.slot_result)
        self.buttonBox__reset.clicked.connect(self.reset)

    @property
    def keyword(self):
        return self.textedit__keyword.toPlainText()

    @property
    def find_keyword(self):
        keyword = self.textedit__keyword.toPlainText()
        return re.compile(f'.*{re.escape(keyword)}.*', re.IGNORECASE)

    def slot_open(self):
        dir = QtWidgets.QFileDialog.getExistingDirectory(self, 'Open Directory', '/data/TD_C')
        self.textBrowser__targetpath.setPlainText(dir)
        return dir

    @property
    def open_path(self):
        tpath = self.textBrowser__targetpath.toPlainText()
        return pathlib.Path(tpath)

    def slot_save(self):
        files = QtWidgets.QFileDialog.getSaveFileName(
            self, 'Save File', '/home/rapa', 'TEXT(*.txt)'
        )
        # fpath = files[0]
        # fpath = pathlib.Path(fpath)
        # print(type(files[0]))
        self.textBrowser__save.setPlainText(files[0])
        # self.write_file(fpath)

    @property
    def save_path(self) -> pathlib.Path:
        spath = self.textBrowser__save.toPlainText()
        return pathlib.Path(spath)

    @property
    def get_file_lst(self) -> list[pathlib.Path]:
        return list(self.open_path.glob('*.*'))

    def open_file(self, n_path:pathlib.Path) -> list:
        source = []
        with open(n_path.as_posix(), 'r') as fp:
            source += fp.readlines()
            result = ''.join(source)
        return result

    @staticmethod
    def make_final(final_path: pathlib.Path, data:list) -> None:
        with open(final_path, 'w') as fp:
            fp.write('\n'.join(data))

    def slot_result(self):
        save_path = self.save_path
        final = []
        for fin in self.get_file_lst:
            if self.find_keyword.search(fin.name):
                final += ['경로 : {0} \n파일명 : {1} \n내용:\n{2} \n{3}\n'.
                format(fin.as_posix(), fin.name, self.open_file(fin), '='*50)]
            if len(final) == 0:
                self.textBrowser_result.setPlainText('검색 결과가 존재하지 않습니다.')
            else:
                self.textBrowser_result.setPlainText('검색이 끝났습니다.')
                self.make_final(f'{save_path.as_posix()}', final)
    def reset(self):
        self.textedit__keyword.clear()
        self.textBrowser__targetpath.clear()
        self.textBrowser__save.clear()
        self.textBrowser_result.clear()

if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)
    find = GUI()
    find.show()
    sys.exit(app.exec_())

