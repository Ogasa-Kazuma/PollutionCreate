
############################ ライブラリ ###################################

#システム関連モジュール
import importlib
import sys
import os
from pathlib import Path

sys.path.append(os.pardir + "/Python")

#描画モジュール
import matplotlib.pyplot as plt
import class_pollution_state_drawer_2D

import Function_Objects
from Function_Objects import AdjustAspectEqu

#計算用モジュール
import random
import numpy as np
import math

#コンテナ管理用モジュール
from itertools import chain
import copy

#汚染源モジュール
import Pollution_Origin
from Pollution_Origin import PollutionOrigin
import Origin_Creater

#汚染の時間変化計算モジュール
import Calculator_Of_Pollutions_Around_Origin
from Calculator_Of_Pollutions_Around_Origin import CalculatorOfPollutionsAroundOrigin
import Origin_History_Creater


#時間モジュール
import time
import datetime

#データ保存ディレクトリ作成モジュール
import Directory_Maker
import Daily_Name_Directory_Maker

#データ保存用モジュール
import Data_Recorder


#モジュールの内容の変更を適用
importlib.reload(Pollution_Origin)
importlib.reload(Calculator_Of_Pollutions_Around_Origin)
importlib.reload(Data_Recorder)
importlib.reload(Origin_Creater)

importlib.reload(class_pollution_state_drawer_2D)
importlib.reload(Function_Objects)
importlib.reload(Origin_History_Creater)

importlib.reload(Directory_Maker)
importlib.reload(Daily_Name_Directory_Maker)
#######################################################################



def ConvertPollutionsToSave(xlim, ylim, pollutions):
    """濃度データを保存できる形式に変換"""
    new_x = []
    new_y = []
    new_pollutions = []

    for x_count in range(xlim):
        for y_count in range(ylim):
            new_x.append(x_count)
            new_y.append(y_count)
            new_pollutions.append(pollutions[x_count][y_count])

    return new_pollutions


#########################################################################################
def main():

    #データ保存用のディレクトリを作成
    dirMaker = Directory_Maker.DirectoryMaker()
    dailyNameDirMaker = Daily_Name_Directory_Maker.DailyNameDirectoryMaker(dirMaker)
    saveDir = dailyNameDirMaker.MkDir("DataLog")

    #探索モデルのパラメータ
    fieldX = 100
    fieldY = 100
    searchingFirstTime = 1000
    searchingLastTime = 4000

    pollutions = np.zeros((fieldX, fieldY))




#############汚染源を作成####################
    origins = list()
    historyCreater = Origin_History_Creater.OriginHistoryCreater()
    originCreater = Origin_Creater.OriginCreater(Pollution_Origin.PollutionOrigin, historyCreater)

    origin1 = originCreater.Create(dict(x = 0, y = 80, startHistory = 100,\
                        t_max = 4000, maxCycleTime = 20, changePerSec = 1))
    origin2 = originCreater.Create(dict(x = 0, y = 10, startHistory = 100,\
                        t_max = 4000, maxCycleTime = 20, changePerSec = 1))
    origins.append(origin1)
    origins.append(origin2)
##################################################




 ########################## 時間変化に応じた濃度分布を計算 #####################################

    decreasingRatio = 1 #汚染源中心からの距離と濃度の減少比
    flowSpeed_ms = 1 #流れの速度




    for t_i in range(searchingFirstTime, searchingLastTime, 1):

        confusedPollutions = np.zeros((fieldX, fieldY))
        #1秒分の濃度分布変化を計算、保存
        for origin_i in origins:
            calculator = CalculatorOfPollutionsAroundOrigin(origin_i)
            pollutionsDist = calculator.CalcDist(fieldX, fieldY, t_i, decreasingRatio, flowSpeed_ms)
            #複数の汚染源を足し合わせる
            confusedPollutions += pollutionsDist

        #500秒ごとに濃度分布を表示
        if(t_i == 1000 or t_i == 1500 or t_i == 2000 or t_i == 2500 or t_i == 3000 or t_i == 3500 or t_i == 3999):
            fig = plt.figure()
            ax = fig.add_subplot(111)
            ax.set_xlabel("x [m]")
            ax.set_ylabel("y [m]")
            aspectObj = AdjustAspectEqu("equal", ax)
            drawer2D = class_pollution_state_drawer_2D.PollutionScatterDrawer2D(ax)
            drawer2D.ApplyAppearanceFuncs(aspectObj)
            drawer2D.draw_pollution_map(fieldX, fieldY, confusedPollutions, cmap_ = "binary")
            fileNameEnd = str(input())
            file = "Pic_Pollution/thesis/cycle/" + str(t_i - 1000) + "_" + fileNameEnd + ".png"
            fig.savefig(file)

        #1ごとにデータ保存
        dataRecorder = Data_Recorder.DataRecorder("..")
        indexes = ["pollutions", "x", "y", "start_t", "end_t"]
        pollutionsToSave = ConvertPollutionsToSave(xlim = fieldX, ylim = fieldY, pollutions = confusedPollutions)
        #pollutionsToSave = list(chain(*confusedPollutions))
        values = [pollutionsToSave, [fieldX], [fieldY], [0], [searchingLastTime - searchingFirstTime]]
        dataRecorder.Record(indexes, values)
        fileName = str(t_i - searchingFirstTime)
        dataRecorder.SaveAsPickle(saveDir + fileName)
        dataRecorder.DropAll()

################################################################################


if __name__ == "__main__":
    main()
