
import matplotlib.pyplot as plt

class AdjustAspectEqu():
    def __init__(self, option, axObj):
        self.__obj = axObj
        self.__aspect = str(option)

    def func(self):
        self.__obj.set_aspect(self.__aspect)
