

import copy
import common
import numpy as np
import importlib
import Pollution_Origin
from Pollution_Origin import PollutionOrigin



importlib.reload(common)
importlib.reload(Pollution_Origin)

class CalculatorOfPollutionsAroundOrigin:

    def __init__(self, originObj):


        self.__originObj = originObj


    def CalcDist(self, xlim_m, ylim_m, time_sec, decreasingRatio, flowSpeed_ms):
        """汚染源周りの汚染濃度についての時間変化を計算するメソッド"""
        #print("流れの速さと濃度減少率の比は" + str(decreasingRatio / flowSpeed) + "です")
        pollutionsDist = np.zeros((xlim_m, ylim_m))

        #汚染源の濃度履歴と汚染源位置を取得
        pollutionsHistory = self.__originObj.GetHistory()
        originX = self.__originObj.GetX()
        originY = self.__originObj.GetY()

        for x in range(xlim_m):
            for y in range(ylim_m):
                distanceFromOrigin_m = common.CalculateAbsoluteDistance(originX, originY, x, y)
                #TODO flowSpeedは、「過去の流れ速度リスト」の平均を取ったものに変更する
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







    #
    #
    # def CalculaPollutionStateAtSomePoint(pollutions, nowTime, originObject, coefficient):
    #
    #     pollutions = copy.deepcopy(pollutions)
    #
    #     xlim, ylim = pollutions.shape
    #
    #     maxPollution = originObject.GetMaxPollution()
    #     originPollutions = originObject.GetOriginPollutions()
    #     originPollutionsBeforeStart = originObject.GetOriginPollutionsBeforeStart()
    #     effectiveLength = originObject.GetEffectiveAreaLength()
    #     originX = originObject.GetOriginX()
    #     originY = originObject.GetOriginY()
    #
    #
    #     #1メートルごとの濃度減少量
    #     decreasingRatio = maxPollution / effectiveLength
    #     #汚染物質の移動速度と1メートルごとの濃度減少量の関係性
    #     pollutionMovingCoefficient = 1
    #     #1mごとの濃度の低下が大きいほど流れが遅く、1mごとの濃度の低下が少ないほど流れが早い傾向
    #     #（その場にとどまらずに流れでどんどん流されるので1メートルごとの低下率が低い)
    #     flowSpeed = pollutionMovingCoefficient / decreasingRatio
    #
    #
    #
    #     for x in range(xlim):
    #         for y in range(ylim):
    #             distanceFromOrigin = CalculateAbsoluteDistance(originX, originY, x, y)
    #
    #             #汚染源の影響範囲外は濃度の割り当てを行わない
    #             if(distanceFromOrigin >= effectiveLength):
    #                 continue;
    #
    #             #TODO flowSpeedは、「過去の流れ速度リスト」の平均を取ったものに変更する
    #             timeToRefference = nowTime - distanceFromOrigin / flowSpeed #何秒前の汚染源中心の濃度を参考にするか
    #             #print("x" + str(x) + "y" + str(y) + "timeRef" + str(timeToRefference))
    #             #参考にしたい時間がスタート前のものならスタート前の汚染源中心濃度値の値をつかう
    #             if(timeToRefference < 0):
    #                 #check 参照濃度リストのインデックスにマイナスをつけてある
    #                 pollutions[x][y] = originPollutionsBeforeStart[-int(abs(timeToRefference))] - decreasingRatio * distanceFromOrigin
    #                 #print(originPollutionsBeforeStart[-int(abs(timeToRefference))])
    #             if(timeToRefference >= 0):
    #                 pollutions[x][y] = originPollutions[int(timeToRefference)] - (decreasingRatio * distanceFromOrigin)
    #                 #print(timeToRefference)
    #             if(pollutions[x][y] < 0):
    #                 pollutions[x][y] = 0
    #
    #
    #
    #                 #concentration = originPollutions[time] - decreasingRatio * distanceFromOrigin
    #                 #pollutions[x][y] = concentration
    #
    #
    #
    #     return pollutions
