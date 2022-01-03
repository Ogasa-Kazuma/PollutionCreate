
import Pickle_Reader
import importlib
import sys
import Pollution_Data_Reader2D
from Pollution_Data_Reader2D import PollutionDataReader2D

importlib.reload(Pickle_Reader)
importlib.reload(Pollution_Data_Reader2D)


def main():


    pklReader = Pickle_Reader.PickleReader()
    dataReader = PollutionDataReader2D(pklReader)
    file = dataReader.read("/home/kazuma/研究/Test/DataLog/2021年/11月/21日/15時/45分/51秒/1001.pkl", 99 , 50 , 0)
    file = dataReader.read("/home/kazuma/研究/Test/DataLog/2021年/11月/21日/15時/45分/51秒/3001.pkl", 99 , 50 , 0)
    file = dataReader.read("/home/kazuma/研究/Test/DataLog/2021年/11月/21日/15時/45分/51秒/2901.pkl", 99 , 50 , 0)
    file = dataReader.read("/home/kazuma/研究/Test/DataLog/2021年/11月/21日/15時/45分/51秒/1501.pkl", 99 , 50 , 0)
    file = dataReader.read("/home/kazuma/研究/Test/DataLog/2021年/11月/21日/15時/45分/51秒/2730.pkl", 99 , 50 , 0)
    file = dataReader.read("/home/kazuma/研究/Test/DataLog/2021年/11月/21日/15時/45分/51秒/1001.pkl", 99 , 50 , 0)
    print(file)


if __name__ == "__main__":
    main()
