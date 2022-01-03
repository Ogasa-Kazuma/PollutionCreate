


class OriginCreater:

    def __init__(self, originClass, historyCreater):
        self.__originClass = originClass
        self.__historyCreater = historyCreater


    def Create(self, args):
        x = args['x']
        y = args['y']
        startHistory = args['startHistory']
        maxTime = args['t_max']
        maxCycleTime = args['maxCycleTime']
        changePerSec = args['changePerSec']
        history = self.__historyCreater.Create(startHistory, maxTime, maxCycleTime, changePerSec)

        origin = self.__originClass(x, y, history)

        return origin
