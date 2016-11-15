import math
from likelihood import *
from sonic import *
from normal import *
from turn import *
from gostraight import *
from particleUpdate import *

def mcl(oldParticles):
    z = getSonar()
    if (z == -1):
        print "Skipping MCL as sonar distance is unreliable"
        return False
    newParticles = []
    for particle in oldParticles:
        likelihood = calculate_likelihood(particle[0],particle[1],particle[2],z)
        newWeight = likelihood * particle[3]
        newParticle = (particle[0],particle[1],particle[2],newWeight)
        newParticles.append(newParticle)
    normalisedParticles = normalisation(newParticles)
    resampledParticles = resampling(normalisedParticles)
    particles = resampledParticles
    return True
    

def navigateToWayPoint(wx, wy, currentPosition, particles):
    cx = currentPosition[0]
    cy = currentPosition[1]
    ctheta = math.radians(currentPosition[2]) #We store the theta in degree

    distance = math.hypot(wx - cx, wy - cy)#This is the main distance
    angle = math.atan2(wy - cy, wx - cx) - ctheta #math.atan2 returns in radians
    print "angle to turn is " + str(angle)
    
    turn(math.degrees(angle))
    particles = [updateRotation(particles[i],math.degrees(angle))for i in range(numberOfParticles)]
    
    gostraight = go()
    gostraight.run(distance)
    particles = [update(particles[i],distance)for i in range(numberOfParticles)]

    #update particles
    mcl(particles)
    
    return particles
