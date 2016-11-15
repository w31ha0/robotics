import brickpi
import time
from config import *

def turn(degrees):
    angleFor90Deg = float(14.55)
    angleToTurn = (degrees/90)*angleFor90Deg
    prevAngle = interface.getMotorAngles(motors)[0][0] 
    interface.increaseMotorAngleReferences(motors,[angleToTurn,-angleToTurn],[6,-6])
    while not interface.motorAngleReferencesReached(motors):
        time.sleep(0.1)
    print 'Turning finished'
    