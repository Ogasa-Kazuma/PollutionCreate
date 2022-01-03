
class PollutionOrigin:


    def __init__(self, x, y, history):

        self.__x = x
        self.__y = y

        self.__history = history

    def GetX(self) -> int:
        return self.__x

    def GetY(self) -> int:
        return self.__y

    def GetHistory(self) -> list:
        return self.__history
