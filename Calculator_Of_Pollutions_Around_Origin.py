

import copy

import numpy as np
import importlib
import math
import Pollution_Origin
from Pollution_Origin import PollutionOrigin



importlib.reload(Pollution_Origin)

class CalculatorOfPollutionsAroundOrigin:

    def __init__(self, originObj):


        self.__originObj = originObj


    def CalcDist(self, xlim_m, ylim_m, time_sec, decreasingRatio, flowSpeed_ms):
        """汚染源周りの汚染濃度についての時間変化を計算するメソッド"""
        pollutionsDist = np.zeros((xlim_m, ylim_m))

        #汚染源の濃度履歴と汚染源位置を取得
        pollutionsHistory = self.__originObj.GetHistory()
        originX = self.__originObj.GetX()
        originY = self.__originObj.GetY()

        for x in range(xlim_m):
            for y in range(ylim_m):
                distanceFromOrigin_m = self.__CalculateAbsoluteDistance(originX, originY, x, y)

                t_ref = time_sec - distanceFromOrigin_m / flowSpeed_ms #何秒前の汚染源中心の濃度を参考にするか
                #汚染源の濃度履歴を参照し、現在位置の濃度を計算
                if(t_ref < 0):
                    print("参照したい時刻での濃度履歴がありません。開始のタイミングを遅くしてください")
                    continue
                if(t_ref >= 0):
                    decAmount =  decreasingRatio * distanceFromOrigin_m
                    pollutionsDist[x][y] = pollutionsHistory[int(t_ref)] - decAmount

                #汚染源の影響が及ばない範囲
                if(pollutionsDist[x][y] < 0):
                    pollutionsDist[x][y] = 0

        return pollutionsDist


    def __CalculateAbsoluteDistance(self, xBegin, yBegin, xEnd, yEnd):

        diff = math.sqrt((xEnd - xBegin) * (xEnd - xBegin) + (yEnd- yBegin) * (yEnd - yBegin))

        return  diff
