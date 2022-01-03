
import I_Pollution_Data_Reader2D
from I_Pollution_Data_Reader2D import I_PollutionDataReader2D

import importlib

importlib.reload(I_Pollution_Data_Reader2D)

class PollutionDataReader2D(I_PollutionDataReader2D):
    def __init__(self, fileReader):
        self.__fileReader = fileReader

    def read(self, path, x, y, t):
        loadedFile = self.__fileReader.load(path)
        ylim = loadedFile["y"][0]

        poll = loadedFile["pollutions"][ylim * x + y]

        return poll
