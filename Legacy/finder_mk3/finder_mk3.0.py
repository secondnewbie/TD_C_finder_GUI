#!/usr/bin/python3
#encoding=utf-8

import pathlib
import re

# 3 목표 : 파일 검색하기
# 3.1 목표 : 검색한 파일의 파일명을 새 txt 파일에 저장하기
# 3.2 목표 : 검색한 파일과 그 내용을 새 txt 파일에 저장하기
# 3.3 목표 : 검색어를 사용자가 직접 입력할 수 있도록

class Finder_mk3:
    def __init__(self, n_path: str) -> None:
        self.__tar_path = pathlib.Path(n_path)
        self.__pattern = re.compile(r'.*test_c.*')

    # 소멸자 임시 주석처리
    # def  __del__(self): -> None:
    #     pass

    @staticmethod
    def get_home_path() -> pathlib.Path:
        """
        :return: 홈 디렉토리 반환
        """
        return pathlib.Path.home()

    #getter
    def get_n_path(self) -> pathlib.Path:
        """
        :return: 타겟 경로
        """
        return self.__tar_path

    #setter
    def set_n_path(self, n_path: pathlib.Path) -> None:
        """
        :param n_path: 타겟 경로
        :return: None
        """
        assert isinstance(n_path, pathlib.Path)
        self.__tar_path = n_path

    @property
    def get_file_lst(self) -> list[pathlib.Path]:
        """
        :return: 타겟 디렉토리 내의 파일만을 찾아 파일명을 리스트로 저장
        """
        fl=[]
        for f in self.__tar_path.glob('*.*'):
            if f.is_file():
                fl.append(f.name)
        return fl

    def choose_file(self, data:list ) -> list[list]:
        fn = []
        # fn = self.__pattern.findall(data)
        # print(fn)
        # fn.append(self.__pattern.findall(data))
        # print(fn)
        for n in data:
            if self.__pattern.search(n):
                fn.append(self.__pattern.search(n).group())
                # fn.append(self.__pattern.search(n)[0])
                # fn.append(self.__pattern.search(n))
                # fn.append(self.__pattern.findall(n))
        return fn

    def writter(self):
        """
        :return: 검색어로 찾은 파일 목록
        """
        fold = []
        for fin in self.choose_file(self.get_file_lst):
            fold.append(fin)
        print(fold)


if __name__=='__main__':
    fdn = Finder_mk3('/data/TD_C/test')

# x=pathlib.Path('/data/TD_C/test')
#
# for f in x.glob('*.*'):
#     if f.is_file():
#         fl=[]
#         fl.append(f.name)
#         print(fl)

# x=pathlib.Path('/data/TD_C/test')
# print(x.name)

# pattern = re.compile('test_c')
# list=['test_c, test_cb, test, ctest_c']
# print(type(list))
# print(pattern.search(list))

# fdn.choose_file(['test_c.txt', 'test_cb.py', 'test.txt', 'ctest_c'])

# print(fdn.get_file_lst)
# fdn.choose_file(fdn.get_file_lst)
fdn.writter()