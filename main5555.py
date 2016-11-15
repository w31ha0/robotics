import brickpi
import math
import particleDataStructure as pds
from config import *
import particleUpdate as pu 
from navigateToWayPoint import *

waypoint1 = (84,30)
waypoint2 = (180,30)
waypoint3 = (180,54)
waypoint4 = (138,54)
waypoint5 = (138,168)
waypoint6 = (114,168)
waypoint7 = (114,84)
waypoint8 = (84,84)
waypoint9 = (84,30)

waypoints = [waypoint2,waypoint3,waypoint4,waypoint5,waypoint6,waypoint7,waypoint8,waypoint9]

def breakdownAndNavigateToWayPoint(waypoint,particles):
    currentPosition = pu.getCurrentPosition(particles)
    print "Current Position is " + str(currentPosition)
    step = 20.0
    
    distance = math.hypot(waypoint[0]-currentPosition[0],waypoint[1]-currentPosition[1])
    gradient = (waypoint[1]-currentPosition[1])/(waypoint[0]-currentPosition[0])
    
    print "distance is  " + str(distance)
    print "gradient is  " + str(gradient)
    
    ctheta = math.radians(currentPosition[2])
    angle = math.atan2(waypoint[1]-currentPosition[1], waypoint[0] - currentPosition[0]) - ctheta 
    print "need to turn " + str(angle)
    #math.atan2 returns in radians    
    dy = math.sin(angle)*step    
    dx = math.cos(angle)*step
    
    print "dx is  " + str(dx)
    print "dy is  " + str(dy)
    
    steps = int(distance/step)
    remainingDistance = distance%step
    
    for i in range(1,steps+1):
    
        particles = navigateToWayPoint(currentPosition[0]+dx,currentPosition[1]+dy,currentPosition,particles)
        currentPosition = getCurrentPosition(particles)
        print "Current Position is " + str(currentPosition)
        canvas.drawParticles(particles)
        
    #dy = math.sin(theta)*remainingDistance    
    #dx = math.cos(theta)*remainingDistance
    particles = navigateToWayPoint(waypoint[0],waypoint[1],currentPosition,particles)
    return particles

canvas = pds.Canvas()
mymap = pds.Map()
pds.drawWall(mymap, canvas)

particles = [initialPosition for i in range(numberOfParticles)]  
canvas.drawParticles(particles)

for waypoint in waypoints:
    particles = breakdownAndNavigateToWayPoint(waypoint,particles)
    #particles = navigateToWayPoint(waypoint[0],waypoint[1],pu.getCurrentPosition(particles),particles)