


import importlib
import Origin_History_Creater


importlib.reload(Origin_History_Creater)



historyCreater = Origin_History_Creater.OriginHistoryCreater()
history = historyCreater.Create(firstConcent = 30, maxTime = 200, maxCycleTime = 20, maxChangePerSec = 0.3)
print(history)

test = list()
test.append(1)
print(test[-1])
print(len(test))
