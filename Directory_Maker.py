

import os
import importlib

class DirectoryMaker():
    """ ディレクトリを作成するクラス """

    def __init__(self):
        pass

    def MkDir(self, pathAndName):
        dir = pathAndName
        #ディレクトリがすでに存在するなら何もしない（上書きもしない）
        if(os.path.isdir(dir)):
            pass
        else:
            os.makedirs(dir)
