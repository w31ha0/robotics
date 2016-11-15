import random 

def normalisation(particles):
    #print "particles are " + str(particles)
    sum = 0.0
    for particle in particles:
        sum += particle[3] 
    new_list = []
    for particle in particles:
        part = list(particle)
        new_weight = part[3]/sum
        part[3] = new_weight 
        part = tuple(part)
        new_list.append(part)
    return tuple(new_list)


def resampling(particles):
    weights = 0
    new_list = []
    for particle in particles:      
        part = list(particle)
        holder = part[3]
        part[3] += weights
        new_list.append(part)
        weights += holder
    
    next_list = []
    x = len(new_list)
    for index in range(x):
        r = random.uniform(0,1)
        for item in new_list:
            if r <= item[3]:
                next_list.append(item)
                break
    for entries in next_list:
        entries[3]=1.0/x

    return(next_list)