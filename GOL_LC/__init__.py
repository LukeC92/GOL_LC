"""
Luke Carroll's implementation of The Game Of Life.

My attempt at an implementation of the Game of Life. The end target is for you to be able iterate the game step by step or run it indefinitely.

"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation
from PIL import Image
np.set_printoptions(threshold=np.inf)

#blip = np.zeros((5,5))
#blip[1,2] = 1
#blip[2,2] = 1
#blip[3,2] = 1




def sumcells(x, y, A):
    """
    This gives the number of living cells adjacent to cell A[x,y].
    
    Parameters
    ----------
    x : int
        The x index of the cell being considered
    y : int
        The y index of the cell being considered
    A : np.array
        The GOL board to iterate
    
    """
    if(y==0):
        if(x==0):
            return A[x+1, y]+A[x+1,y+1]+A[x,y+1]
        elif(0<x<A.shape[0]-1):
            return A[x-1,y]+A[x-1,y+1]+A[x,y+1]+A[x+1,y+1]+A[x+1,y]
        elif(x==A.shape[0]-1):
            return A[x-1,y]+A[x-1,y+1]+A[x,y+1]
    elif(0<y<A.shape[1]-1):
        if(x==0):
            return A[x,y-1]+A[x,y+1]+A[x+1,y-1]+A[x+1,y]+A[x+1,y+1]
        elif(0<x<A.shape[0]-1):
            return A[x-1,y-1]+A[x-1,y]+A[x-1, y+1]+A[x,y-1]+A[x,y+1]+A[x+1,y-1]+A[x+1,y]+A[x+1,y+1]
        elif(x==A.shape[0]-1):
            return A[x-1,y-1]+A[x-1,y]+A[x-1, y+1]+A[x,y-1]+A[x,y+1]
    elif(y==A.shape[1]-1):
        if(x==0):
            return A[x,y-1]+A[x+1,y-1]+A[x+1,y]
        elif(0<x<A.shape[0]-1):
            return A[x-1,y-1]+A[x-1,y]+A[x,y-1]+A[x+1,y-1]+A[x+1,y]
        elif(x==A.shape[0]-1):
            return A[x-1,y-1]+A[x-1,y]+A[x,y-1]


    
    #else
        #return -999 wanted to just use the first if statement and restrict things so the system only operates within aA 1 cell buffer around the edge
    



def alive(x, y, A):
    """
    This function determines if aA cell is alive or dead in the next iteration.
    
    Parameters
    ----------
    x : int
        The x index to use
    y : int
        The y index to use
    A : np.array
        The GOL board to iterate
        
    """
    v = A[x,y]
    t = sumcells(x,y,A)
    return ((v==1 and t in [2,3]) or (v==0 and t==3))
    
    
    #if((v=1 and t=2,3) or (v=1 and t=3))
       #return true
    #else if((v=1 and t!=2,3) or (v=0 and t!=3))
        #did have statement saying t!=-999 cause of error in previous tactic where I restricted the functions behaviour to within aA boundary
        #return false
    #else return "You've done something wrong" now largely useless as 
    
    
def updatecell(x,y, A):
    if(alive(x,y,A)): return 1
    else: return 0
    



def update(A):
    B = np.copy(A)
    for i in range(0, B.shape[0]):
        for j in range(0,B.shape[1]):
            B[i,j]=updatecell(i,j,A)
    return B





if __name__ == '__main__':
    blip = np.zeros((5,5))
    blip[1,2] = 1
    blip[2,2] = 1
    blip[3,2] = 1
    
    
    blip_update = np.zeros((5,5))
    blip_update[2,1] = 1
    blip_update[2,2] = 1
    blip_update[2,3] = 1
    
    gliderG = np.array([[ 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ],[ 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ],
  [ 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0 ],
  [ 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0 ],
  [ 0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0 ],
  [ 0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0 ],
  [ 0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ],
  [ 0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0 ],
  [ 0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0 ],
  [ 0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ],
  [ 0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ],
  [ 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ],[ 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ]])
    
    #print(gliderG)
    
    
    # Using this GIF: http://www.videogamesprites.net/FinalFantasy1/Party/Before/Fighter-Front.gif

    
    
    a = Image.open('/home/h05/lcarroll/Documents/Learning Python/Gospers_glider_gun.gif')
    b = Image.open('/home/h05/lcarroll/Documents/Learning Python/start of glider.png')
    c = Image.open('/home/h05/lcarroll/Documents/Learning Python/Gospers_glider_gun_firstframe.jpg')
    
    #a.show()
    c.show()
#    transparency = a.info['transparency'] 
#    a.save('test1.png', transparency=transparency)
#    
#    a.seek(a.tell()+1)
#    transparency = a.info['transparency'] 
#    a.save('test2.png', transparency=transparency)
    
    # First frame comes out perfect, second frame (test2.png) comes out black,
    # but in the "right shape", ie 
    # http://i.stack.imgur.com/5GvzC.png
    
    
#    print(type(a))
#    print(a.tell())
#    print(a.size)
    print(c.size)

    #print(list(a.getdata()))
    aA = np.array(a.getdata())
    aS = aA.reshape(250,180)
    aR = abs(aS-1)
    bA = np.array(b.getdata())
    cA = np.array(c.getdata())     
    cAB = np.array(c)
    c1 = cAB//200
    #c0 = abs(c1-1)
    c0 = (cAB<200).astype(np.uint8)
    c0 = c0[::-4,::4]
#    print(aA.shape)
    print(cA.shape)
    print(cAB.shape)

    print(cAB)
    

    


    #print(b.getdata())

    #print(type(bA))


  
    

    

    
    #print(cA)
    #print(aR)
    #print(cAB)
    #print(c1)
    #print(c0)
    
    
#    def iter_frames(a):
#        try:
#            i= 0
#            while 1:
#                a.1seek(i)
#                imframe = a.copy()
#                if i == 0: 
#                    palette = imframe.getpalette()
#                else:
#                    imframe.putpalette(palette)
#                yield imframe
#                i += 1
#        except EOFError:
#            pass
#
#            for i, frame in enumerate(iter_frames(a)):
#                frame.save('test%bA.png' % i,**frame.info)
                



    fig, ax = plt.subplots()
    
    
    graph = ax.pcolormesh(c0, cmap='Greys')
    plt.grid(color='black')
    
    
    
    def animate(B):
        B[:] = update(B)
        C = B.flatten()
        graph.set_array(C)

        return graph,
    
    
    #The useer thought out this was unnecessary, turns out it is necessary.
    def init():
        return graph,
    
    
    
    ani = animation.FuncAnimation(fig, animate, [c0], init_func=init, interval=100, blit=False)
    plt.show()
    
    
    
    

    

        
