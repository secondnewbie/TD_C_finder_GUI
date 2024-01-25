#!/usr/bin/python3
# encoding=utf-8

import sys
import pathlib
import re
from PySide2 import QtWidgets, QtGui, QtCore
import Finder_mk3_ui
import importlib
import Result_viewer

importlib.reload(Finder_mk3_ui)


def open_file(n_path: pathlib.Path) -> str:
    source = []
    with open(n_path.as_posix(), 'r') as fp:
        source += fp.readlines()
        result = ''.join(source)
    return result


class GUI(QtWidgets.QWidget, Finder_mk3_ui.Ui_Form):
    def __init__(self, parent=None) -> None:
        super(GUI, self).__init__(parent)

        self.setupUi(self)

        self.__viewer = Result_viewer.Viewer()

        self._signal_func()

        self.get_recent_lst()



    def _signal_func(self) -> None:
        self.buttonBox__targetpath.clicked.connect(self.slot_open)
        self.buttonBox__save.clicked.connect(self.slot_save)
        self.buttonBox__ok.clicked.connect(self.slot_result)
        self.buttonBox__reset.clicked.connect(self.reset)
        self.__viewer.buttonBox__close.clicked.connect(self.close_window)
        # self.comboBox__recent.currentTextChanged.connect(self.open_window)
        self.comboBox__recent.currentIndexChanged.connect(self.open_cache)

    @property
    def keyword(self) -> str:
        return self.textedit__keyword.toPlainText()

    @property
    def find_keyword(self) -> re.Pattern[str]:
        keyword = self.textedit__keyword.toPlainText()
        return re.compile(f'.*{re.escape(keyword)}.*', re.IGNORECASE)

    def slot_open(self) -> str:
        dir = QtWidgets.QFileDialog.getExistingDirectory(self, 'Open Directory', '/data/TD_C')
        self.textBrowser__targetpath.setPlainText(dir)
        return dir

    @property
    def open_path(self) -> pathlib.Path:
        tpath = self.textBrowser__targetpath.toPlainText()
        return pathlib.Path(tpath)

    def slot_save(self) -> None:
        files = QtWidgets.QFileDialog.getSaveFileName(
            self, 'Save File', '/home/rapa',
            'All file (*.*);;Text file (*.txt);;Shell file (*.sh);;Json file (*.json)')
        self.textBrowser__save.setPlainText(files[0])

    @property
    def save_path(self) -> pathlib.Path:
        spath = self.textBrowser__save.toPlainText()
        return pathlib.Path(spath)

    @property
    def get_file_lst(self) -> list[pathlib.Path]:
        return list(self.open_path.glob('*.*'))

    @staticmethod
    def make_final(final_path: pathlib.Path, data: list) -> None:
        with open(final_path, 'w') as fp:
            fp.write('\n'.join(data))

    def slot_result(self) -> None:
        if len(self.keyword) == 0:
            self.textBrowser_result.setPlainText('검색어를 입력하세요.')
        else:
            save_path = self.save_path
            final = []
            for fin in self.get_file_lst:
                if self.find_keyword.search(fin.name):
                    final += ['경로 : {0} \n파일명 : {1} \n내용:\n{2} \n{3}\n'.
                              format(fin.as_posix(), fin.name, open_file(fin), '=' * 60)]
                if len(final) == 0:
                    self.textBrowser_result.setPlainText('검색 결과가 존재하지 않습니다.')
                else:
                    self.textBrowser_result.setPlainText('검색이 끝났습니다.')
                    self.make_final(f'{save_path.as_posix()}', final)
                    self.buttonBox__ok.accepted.connect(self.open_window)
            self.get_recent_lst()
            # self.cache_lst()

    def reset(self) -> None:
        self.textedit__keyword.clear()
        self.textBrowser__targetpath.clear()
        self.textBrowser__save.clear()
        self.textBrowser_result.clear()
        self.comboBox__recent.clear()
        self.viewer.close()

    @property
    def viewer(self) -> Result_viewer.Viewer:
        return self.__viewer

    @viewer.setter
    def viewer(self, viewer) -> None:
        assert isinstance(viewer, Result_viewer.Viewer)
        self.__viewer = viewer

    def open_window(self) -> None:
        self.viewer.show()
        save_path = self.save_path
        self.write_window(save_path)

    def close_window(self) -> None:
        self.viewer.close()

    def write_window(self, r_path: pathlib.Path) -> None:
        assert isinstance(r_path, pathlib.Path)
        self.viewer.read_file(r_path)

    def get_recent_lst(self, recent=[]) -> None:
        self.comboBox__recent.clear()
        save_path = self.save_path.name
        recent.insert(0, save_path)
        if recent == ['']:
            recent.remove('')
        else:
            pass
        if len(recent) > 3:
            recent = recent[:3]
        self.comboBox__recent.addItems(recent)

    def cache_path(self, cache={}):
        path = self.save_path
        cache.update({path.name: path})
        cache_value = list(cache.values())
        cache_value.reverse()
        num = self.comboBox__recent.currentIndex()
        return cache_value[num]

    def open_cache(self):
        value = self.cache_path()
        v_path = pathlib.Path(value)
        self.write_window(v_path)
        self.viewer.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    find = GUI()
    find.show()
    sys.exit(app.exec_())
