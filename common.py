import math

def CalculateAbsoluteDistance(xBegin, yBegin, xEnd, yEnd):

    diff = math.sqrt((xEnd - xBegin) * (xEnd - xBegin) + (yEnd- yBegin) * (yEnd - yBegin))

    return  diff
