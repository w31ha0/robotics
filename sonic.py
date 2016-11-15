import brickpi
import time
from config import *

def getSonar():
    usReadingArr = []
    usReading = interface.getSensorValue(SensorPort)[0]
    for counter in range(0, 10):
        if (usReading > 45 and usReading < 144):
            usReadingArr.append(usReading)
    print usReadingArr
    if (len(usReadingArr) == 0):
        return -1
    elif (len(usReadingArr) == 1):
        return usReadingArr[0]
    else:
        avg = sum(usReadingArr) / len(usReadingArr)
        return avg
    
