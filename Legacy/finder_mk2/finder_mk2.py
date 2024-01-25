#!/usr/bin/python3
#encoding=utf-8

import pathlib


class Finder_mk2:
    def __init__(self, n_path: str) -> None:
        self.__tar_path = pathlib.Path(n_path)
        self.__f_name = "test_c.txt"

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
    def choose_file_name(self) -> list[str]:
        """
        :return: 타겟 디렉토리 내의 '파일'의 파일명만 리스트로 저장
        """
        # map
        # pathlib.Path.glob
        # pathlib.Path.name
        # pathlib.Path.is_file
        # lambda
        for F in self.__tar_path.glob(self.__f_name):
            if not F.is_file():
                continue
            fn = []
            fn.append(F.name)
            return fn

    @property
    def choose_file_path(self) -> pathlib.Path:
        """
        :return: 타겟 디렉토리 내의 '파일'의 경로만 리스트(str)로 저장
        """
        for F in self.__tar_path.glob(self.__f_name):
            if not F.is_file():
                continue
            fp = []
            fp.append(F.as_posix())
            return fp

    @property
    def cor_name(self) -> list[str]:
        """
        :return: choose_file_name의 리스트에서 사용자가 설정한 파일명과
                 동일한 이름의 파일만 리스트(str)로 저장
        """
        ans = []
        for i in self.choose_file_name:
            if i != self.__f_name:
                continue
            ans.append(i)
        return ans
"""
fp = list[타겟 파일의 경로]
ans = list[타겟 파일의 파일명]
"""
    # 타겟 파일의 경로, 이름, 내용을 홈 디렉토리에 'finder_result.txt'로 저장
    def writter(self, n_path: pathlib.Path):
        with open(, 'w')
