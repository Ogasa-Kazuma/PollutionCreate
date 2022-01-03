
import random

class OriginHistoryCreater:


    def __init__(self):
        pass


    def Create(self, firstConcent, maxTime, maxCycleTime, maxChangePerSec):

        history = [firstConcent]
        funcs = [self.__Increase, self.__Decrease]

        f_i = 0
        t = 0

        while(t < maxTime):
            #濃度履歴の最大時間まで濃度の増減を繰り返す
            cycleTime = self.__CycleTime(t, maxTime, maxCycleTime)
            history = self.__CalcOneCycleChange(funcs[f_i], history, cycleTime, maxChangePerSec)

            t += cycleTime
            f_i = self.__SwitchFunc(f_i)



        return history


    def __SwitchFunc(self, number):
        if(number == 0):
            return 1
        elif(number == 1):
            return 0

        raise ValueError('関数テーブルのインデックスが間違っています')


    def __CycleTime(self, nowTime, maxTime, maxCycleTime):
        """濃度履歴の最大時間を超えてしまわないようサイクルタイムを調整"""
        cycleTime = self.__DecideCycleTime(maxCycleTime)
        nextFinishTime = nowTime + cycleTime

        if(nextFinishTime > maxTime):
            cycleTime -= nextFinishTime - maxTime
            return cycleTime

        return cycleTime



    def __CalcOneCycleChange(self, func, history, cycleTime, maxChangePerSec):
        """1サイクルでの濃度変化量を計算"""
        for t_i in range(0, cycleTime):

            latestConcent = func(history[-1], maxChangePerSec)
            history.append(latestConcent)

        return history


    def __Increase(self, ref, maxChangeAmount):
        inc = ref + random.uniform(0, maxChangeAmount)
        return inc


    def __Decrease(self, ref, maxChangeAmount):
        dec = ref - random.uniform(0, maxChangeAmount)
        return dec


    def __DecideCycleTime(self, maxCycleTime):
        """濃度の増減のサイクルをランダムに決定"""
        cycle = random.randint(0, maxCycleTime)
        return cycle
