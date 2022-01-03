# -*- coding: utf-8 -*-

import pandas as pd
import importlib



class PickleReader():

    def __init__(self):
        pass

    def Read(self, path):
        file = pd.read_pickle(str(path))
        return file



# f = pd.read_pickle("DataLog/2021年/9月/16日/12時/37分/46秒/2021_9_16_1238_32.pkl")
# f2 = pd.read_pickle("DataLog/2021年/9月/16日/12時/37分/46秒/2021_9_16_1238_34.pkl")
#
# elementCounts = len(f["pollution"])
#
# test_list = [0 for i in range(elementCounts)]
#
# for i in range(elementCounts):
#     test_list[i] = f["z"][i]
#
#
# print(test_list)
