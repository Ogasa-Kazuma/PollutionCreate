

import time
import datetime

class DailyNameDirectoryMaker():

    def __init__(self, dirMaker):
        self.__dirMaker = dirMaker

    def MkDir(self, parDir):

        dt = datetime.datetime.now()
        pathAndName = str(parDir) + "/" + str(dt.year) + str("年") + str("/") + \
        str(dt.month) + "月/" + str(dt.day) + "日/" + str(dt.hour) + "時/" + str(dt.minute) + "分/" + str(dt.second) + "秒/"

        self.__dirMaker.MkDir(pathAndName)

        return pathAndName
