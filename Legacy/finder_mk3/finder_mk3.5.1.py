#!/usr/bin/python3
#encoding=utf-8

import pathlib
import re

class Finder_mk3:
    def __init__(self, n_path: str) -> None:
        keyword = input("검색어를 입력하세요: ")
        self.__tar_path = pathlib.Path(input("검색할 경로를 입력하세요: "))
        self.__save_path = pathlib.Path(input("저장할 경로를 입력하세요: "))
        self.__pattern = re.compile(f'.*{re.escape(keyword)}.*', re.IGNORECASE)
        self.result_keyword = input("저장할 txt 파일 이름을 입력하세요: ")


    def __del__(self) -> None:
        print('검색을 종료합니다.')



    #getter
    @property
    def n_path(self) -> pathlib.Path:
        """
        :return: 타겟 경로
        """
        return self.__tar_path

    #setter
    @n_path.setter
    def n_path(self, n_path: pathlib.Path) -> None:
        """
        :param n_path: 타겟 경로
        :return: None
        """
        assert isinstance(n_path, pathlib.Path)
        self.__tar_path = n_path

    @property
    def get_file_lst(self) -> list[pathlib.Path]:
        """
        :return: 타겟 디렉토리 내의 파일 만을 찾아 경로 저장
        """
        return(list(self.__tar_path.glob('*.*')))

    def open_file(self, n_path:pathlib.Path) -> list:
        """
        :param data: 파일 경로
        :return: 파일의 내용 전체를 리스트에 담는다.
        """
        source = []
        with open(n_path.as_posix(), 'r') as fp:
            source += fp.readlines()
            result = ''.join(source)
        return result

    @staticmethod
    def make_final(final_path: pathlib.Path, data:list) -> None:
        """
        :param final_path: 새 txt파일을 저장할 경로
        :param data: 검색된 파일의 경로, 파일명, 내용
        :return: 새 txt파일을 만든다.
        """
        with open(final_path, 'w') as fp:
            fp.write('\n'.join(data))

    # 타겟 파일의 경로, 이름, 내용을 홈 디렉토리에 'finder_result.txt'로 저장
    def writter(self):
        """
        :return: 검색어로 찾은 파일 목록을 새 txt파일로 저장
        """
        save_path = self.__save_path
        final = []
        for fin in self.get_file_lst:
            if self.__pattern.search(fin.name):
                final += ['경로 : {0} \n파일명 : {1} \n내용:\n{2} \n{3}\n'.
                        format(fin.as_posix(), fin.name, self.open_file(fin), '='*50)]

        Finder_mk3.make_final(f'{save_path.as_posix()}/{self.result_keyword}.txt', final)

if __name__=='__main__':
    fdn = Finder_mk3('/data/TD_C/test')


fdn.writter()
