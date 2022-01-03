
from abc import ABCMeta, abstractmethod

class I_PollutionDataReader2D(metaclass = ABCMeta):
    @abstractmethod
    def read(file, x, y, t):
        pass
