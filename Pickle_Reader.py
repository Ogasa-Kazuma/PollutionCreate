# -*- coding: utf-8 -*-

import pandas as pd
import importlib



class PickleReader():

    def __init__(self):
        pass

    def Read(self, path):
        file = pd.read_pickle(str(path))
        return file
