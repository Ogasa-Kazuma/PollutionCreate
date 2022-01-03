
import pandas as pd
import datetime
import os
import numpy as np

class DataRecorder:

    def __init__(self, currentDirectory):
        self.__log = pd.DataFrame(index=[], columns=[])

        self.__currentDirectory = str(currentDirectory)

    def AddRemarks(self, remarks):
        logList = list()
        logList.append(remarks)
        testLog = pd.DataFrame(index=[], columns=[])
        testLog["備考欄"] = logList
        self.__log = pd.concat([self.__log, testLog], axis = 1)


    def Record(self, indexNames, values):
        """データの保存を行う関数。csvへの保存はまだ行わない"""
        #保存するインデックス名前と値を対応づける
        for i in range(len(indexNames)):
            datalog = pd.DataFrame(index=[], columns=[])
            #単一の値（非リスト）だと保存できない。そのため、単一の値である場合はリストに変換する
            if(type(values[i]) == list):
                datalog[indexNames[i]] = values[i]
            else: #非リストの場合
                datalog[indexNames[i]] = [values[i]]

            self.__log = pd.concat([self.__log, datalog], axis = 1)

    def AppendRow(self, indexNames, values):
        #保存するインデックス名前と値を対応づける
        for i in range(len(indexNames)):
            datalog = pd.DataFrame(index=[], columns=[])
            #単一の値（非リスト）だと保存できない。そのため、単一の値である場合はリストに変換する
            if(type(values[i]) == list):
                datalog[indexNames[i]] = values[i]
            else: #非リストの場合
                datalog[indexNames[i]] = [values[i]]

            self.__log = pd.concat([self.__log, datalog])


    def SaveAsPickle(self, pathName):
        self.__log.to_pickle(str(pathName) + ".pkl")

    def SaveAsNpz(self, pathName):
        data = np.array(self.__log)
        np.savez(str(pathName) + ".npz", data)

    def SaveAsCsv(self, pathName):
        self.__log.to_csv(str(pathName) + ".csv", index = False,  encoding = 'cp932')

    def DropAll(self):
        self.__log = pd.DataFrame(index=[], columns=[])
