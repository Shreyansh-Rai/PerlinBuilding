import random
from re import L
def genSeed(asize):
    lis=[]
    for i in range(asize) :
        lis.append(random.random())
    return lis


def perlin1d (asize , octaves) :
    seedlist = genSeed(asize)
    perlinlist = []
    for i in range(asize) :
        #we calculate the value for each point as we go in O(n^2)
        noise = 0.0
        scalingfactor = 1.0
        netscale = 0.0

        for j in range(octaves) :
            #now we go ahead and calculate the ocataves per point
            #then we will determine the noise by using the 
            #interpolation formula adjust scale and then pass it into the perlin list
            pitch = asize/(2**j) #pitch is how much we go along our randomlist each time 
            x1 =int( int((i/pitch)) * pitch)
            
            x2 = int((x1+pitch)%asize )

            ratiomoved = (i-x1)/float(pitch)

            inter = (1.0 - ratiomoved)*seedlist[x1] + ratiomoved*seedlist[x2]

            netscale = netscale + scalingfactor
            noise = noise + inter*scalingfactor
            scalingfactor = scalingfactor/2
        
        perlinlist.append(noise/netscale)
    return perlinlist

def perlin2d (asize , octaves) :
    seedlist = genSeed(asize*asize)
   
    perlinlist = [[0]*asize]*asize
    for i in range(asize) :
        #we calculate the value for each point as we go in O(n^2)
        for y in range(asize):
            noise = 0.0
            scalingfactor = 1.0
            netscale = 0.0

            for j in range(octaves) :
                #now we go ahead and calculate the ocataves per point
                #then we will determine the noise by using the 
                #interpolation formula adjust scale and then pass it into the perlin list
                pitch = asize/(2**j) #pitch is how much we go along our randomlist each time 
                x1 =int( int((i/pitch)) * pitch)
                y1 =int( int((y/pitch)) * pitch)
                x2 = int((x1+pitch)%asize )
                y2 = int((x1+pitch)%asize )
                
                ratiomoved = (i-x1)/float(pitch)
                ratiomovedy = (y-y1)/float(pitch)
                
                inter = (1.0 - ratiomoved)*seedlist[y1*asize + x1] + ratiomoved*seedlist[y1*asize+x2]
                inter2 = (1.0 - ratiomoved)*seedlist[y2*asize + x1] + ratiomoved*seedlist[y2*asize + x2]
                netscale = netscale + scalingfactor
                noise = noise + inter*scalingfactor
                scalingfactor = scalingfactor/2
            
            perlinlist[i][y] = (noise/netscale)
    return perlinlist
# l = perlin2d(64,16)

# print(l)
def scale(l) :
    for i in l :
        for j in i:
            j=j*100
    
def findmin(l): 
    min = 1
    for i in l :
        for j in i:
            if min > j :
                min = j
    return min

def shuffle(n,asize,o):
    perlinlist = [[0]*asize]*asize
    for i in range(n):
        l = perlin2d(asize,o)
        for i in range(asize) :
            for j in range(asize):
                if(random.randint(1,2)==1):
                    perlinlist[i][j] += random.random()*l[i][j]
                else:
                    perlinlist[i][j] += random.random()*l[j][i]
    return perlinlist

        




# l= perlin2d(100,120)
# l2=perlin2d(100,120)
# l3 =perlin2d(100,120)
# for i in range(100) :
#     for j in range(100):
#         print((0.2*l[i][j]+0.3*l2[i][j]+0.9*l3[i][j])/2)
# print(findmin(l))