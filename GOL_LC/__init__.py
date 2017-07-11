import numpy as np
import matplotlib.pyplot as plt

blip = np.zeros((5,5))
blip[1,2] = 1
blip[2,2] = 1
blip[3,2] = 1

print("hello")
print(blip)
plt.pcolormesh(blip, cmap='Greys')
plt.grid(color='black')
plt.show()


def sumcells(x, y, A):
    if(y=0)
        if(x=0)
            return A[x+1, y]+A[x+1,y+1]+A[x,y+1]
        else if(0<x<A.shape[0]-1):
            return A[x-1,y]+A[x-1,y+1]+A[x,y+1]+A[x+1,y+1]+A[x+1,y]
        else if(x=A.shape[0]-1):
            return A[x-1,y]+A[x-1,y+1]+A[x,y+1]
    else if(0<y<A.shape[1]-1):
        if(x=0):
            return A[x,y-1]+A[x,y+1]+A[x+1,y-1]+A[x+1,y]+A[x+1,y+1]
        else if(0<x<A.shape[0]-1):
            return A[x-1,y-1]+A[x-1,y]+A[x-1, y+1]+A[x,y-1]+A[x,y+1]+A[x+1,y-1]+A[x+1,y]+A[x+1,y+1]
        else if(x=A.shape[0]-1):
            return A[x-1,y-1]+A[x-1,y]+A[x-1, y+1]+A[x,y-1]+A[x,y+1]
    else if(y=A.shape[1]-1):
        if(x=0):
            return A[x,y-1]+A[x+1,y-1]+A[x+1,y]
        else if(0<x<A.shape[0]-1):
            return A[x-1,y-1]+A[x-1,y]+A[x,y-1]+A[x+1,y-1]+A[x+1,y]
        else if(x=A.shape[0]-1):
            return A[x-1,y-1]+A[x-1,y]+A[x,y-1]

    
    #else
        #return -999 wanted to just use the first if statement and restrict things so the system only operates within a 1 cell buffer around the edge
    


def alive(x, y, A):
    v = A[x,y]
    t = sumcells(x,y,A)
    return ((v=1 and t=2,3) or (v=0 and t=3))
    
    
    #if((v=1 and t=2,3) or (v=1 and t=3))
       #return true
    #else if((v=1 and t!=2,3) or (v=0 and t!=3))
        #did have statement saying t!=-999 cause of error in previous tactic where I restricted the functions behaviour to within a boundary
        #return false
    #else return "You've done something wrong" now largely useless as 
    
    


def update(A):
    B = np.copy(A)
    B[alive(x,y,A)]=1
    B[not alive(x,y,A)]=0
    return B


    
    
#want to take the numbers from sumcells and build a new array filled with 1s and 0s depending on the values of sumcells
    