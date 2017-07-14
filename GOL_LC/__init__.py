"""
Luke Carroll's implementation of The Game Of Life.

My implementation of the Game of Life. By editing the code at the bottom
you can enter a particular starting state. By running the program you
will then see the game play out.

"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation
from PIL import Image
np.set_printoptions(threshold=np.inf)


full = np.ones((5,5))

full_update = np.zeros((5,5))
full_update[0,0]=1
full_update[4,0]=1
full_update[0,4]=1
full_update[4,4]=1

#defining a small array on which the blinker oscillator is plotted
blinker = np.zeros((5,5))
blinker[1,2] = 1
blinker[2,2] = 1
blinker[3,2] = 1

#the state the blinker should be in after 1 generation
blinker_update = np.zeros((5,5))
blinker_update[2,1] = 1
blinker_update[2,2] = 1
blinker_update[2,3] = 1


def sumcells(x, y, A):
    """
    This gives the number of living cells adjacent to cell A[x,y] in the
    current generation.
    
    Parameters
    ----------
    x : int
        The x index of the cell being considered
    y : int
        The y index of the cell being considered
    A : np.array
        The GOL board to iterate
    return : int
        The number of living cells adjacent to cell A[x,y]
    
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
            return A[x-1,y-1]+A[x-1,y]+A[x-1, y+1]+A[x,y-1]+A[x,y+1] \
                   +A[x+1,y-1]+A[x+1,y]+A[x+1,y+1]
        elif(x==A.shape[0]-1):
            return A[x-1,y-1]+A[x-1,y]+A[x-1, y+1]+A[x,y-1]+A[x,y+1]
    elif(y==A.shape[1]-1):
        if(x==0):
            return A[x,y-1]+A[x+1,y-1]+A[x+1,y]
        elif(0<x<A.shape[0]-1):
            return A[x-1,y-1]+A[x-1,y]+A[x,y-1]+A[x+1,y-1]+A[x+1,y]
        elif(x==A.shape[0]-1):
            return A[x-1,y-1]+A[x-1,y]+A[x,y-1]
        
def neighbours(A):
    """
    This function returns an array showing the number of neighbours
    of each cell.
    
    Parameters
    ----------
    A : np.array
        The GOL board who's number of neighbours we are calculating
    return : np.array
        The number of neighbours for each cell
    """
    A0 = np.pad(A,((1,1),(1,1)), mode='constant')
    A1 = A0[0:-2, 0:-2]
    A2 = A0[0:-2, 1:-1]
    A3 = A0[0:-2, 2:]
    A4 = A0[1:-1, 0:-2]
    A5 = A0[1:-1, 2:]
    A6 = A0[2:, 0:-2]
    A7 = A0[2:, 1:-1]
    A8 = A0[2:, 2:]  
    return A1+A2+A3+A4+A5+A6+A7+A8

def alive(x, y, A):
    """
    This function determines if a cell is alive or dead in the next
    generation.
    
    Parameters
    ----------
    x : int
        The x index of the cell being considered
    y : int
        The y index of the cell being considered
    A : np.array
        The GOL board to iterate
    return : bool
        True if A[x,y] should be alive in the next generation, 
        false otherwise.
        
    """
    v = A[x,y]
    t = sumcells(x,y,A)
    return ((v==1 and t in [2,3]) or (v==0 and t==3))



DC = blinker == 1
X = neighbours(blinker)
Y = X == 2
Z = X == 3
LL = np.logical_or(Y, Z)
KK = np.logical_and(LL, DC)
BD = blinker==0
BDL = np.logical_and(BD, Z)
BF = np.logical_or(BDL, KK)

print(X)
print(BF)


def updateM(A):
    """
    This function takes an array and returns the state it will be in
    in the next generation. It does this using array logic.
    
    Parameters
    ----------
    A : np.array
        The array to be updated
    return : np.array
        The state of the array in the next generation.
    """
    live = A==1
    neighbourS = neighbours(A)
    neighbour2 = neighbourS == 2
    neighbour3 = neighbourS == 3
    neighbour2or3 = np.logical_or(neighbour2, neighbour3)
    live2live = np.logical_and(neighbour2or3, live)
    dead = A==0
    dead2live = np.logical_and(dead, neighbour3)
    nowLiving = np.logical_or(dead2live, live2live)
    result = nowLiving.astype(np.uint8)
    return result
   
   
def updatecell(x,y,A):
    """
    This function will return the value a cell should take in the next
    generation of Life
    
    Parameters
    ----------
    x : int
        The x index of the cell being considered
    Y : int
        The y index of the cell being considered
    A : np.array
        The GOL board to iterate
    return : int
        The value A[x,y] should take in the next generation
    """
    if(alive(x,y,A)): return 1
    else: return 0
    
    
def update(A):
    """
    This function will return the state an entered GOL board should be
    in the next generation.
    
    Parameters
    ----------
    A : np.array
        The GOL board to iterate
    return : np.array
        The state the GOL board should be in the next generation
    """
    B = np.copy(A)
    for i in range(0, B.shape[0]):
        for j in range(0,B.shape[1]):
            B[i,j]=updatecell(i,j,A)
    return B



if __name__ == '__main__':
    #a possible representation of the Gosper glider gun found from a 
    #website via Google
    gliderG = np.array([
        [ 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ],
        [ 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ],
        [ 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0 ],
        [ 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0 ],
        [ 0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0 ],
        [ 0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0 ],
        [ 0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ],
        [ 0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0 ],
        [ 0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0 ],
        [ 0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ],
        [ 0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ],
        [ 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ],
        [ 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ]])
    

    #various images relating to the Gosper Glider to be experiement with
    a = Image.open('/home/h05/lcarroll/Documents/Learning Python/Gospers_glider_gun.gif')
    b = Image.open('/home/h05/lcarroll/Documents/Learning Python/start of glider.png')
    c = Image.open('/home/h05/lcarroll/Documents/Learning Python/Gospers_glider_gun_firstframe.jpg')
    
    #a.show()
    #c.show()



#    print(type(a))
#    print(a.tell())
#    print(a.size)
    #print(c.size)

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
#    print(cA.shape)
#    print(cAB.shape)
    #print(b.getdata())
    #print(type(bA))

    #print(cA)
    #print(aR)
    #print(cAB)
    #print(c1)
    #print(c0)
    
    
    #a figure and graph to be used within ani to animate a Game of Life
    fig, ax = plt.subplots()
    graph = ax.pcolormesh(c0, cmap='Greys')
    plt.grid(color='black')
    
    def animate(B):
        """
        This function updates a given array B and graph's input to it, 
        thus animating from one generation to the next
        
        Parameters
        ----------
        B : np.array
            The GOL board to be updated
        return : The updated state of the GOL board
        """
        B[:] = update(B)
        C = B.flatten()
        graph.set_array(C)

        return graph,
    
    
    def animateM(B):
        """
        This function updates a given array B and graph's input to it, 
        thus animating from one generation to the next, this uses
        updateM which uses array logic.
        
        Parameters
        ----------
        B : np.array
            The GOL board to be updated
        return : The updated state of the GOL board
        """
        B[:] = updateM(B)
        C = B.flatten()
        graph.set_array(C)

        return graph,    
    
    
    #The user thought out this was unnecessary, turns out it is necessary.
    def init():
        """
        Sets the initial state for the FuncAnimation. Even though this 
        function changes nothing
        it is necessary to include it for a recursive animation.
        """
        return graph,
    
    
    #animates a game of life with the start state listed as the 3rd 
    #parameter and in graph above
    #ani = animation.FuncAnimation(fig, animate, [c0], init_func=init, 
    #                              interval=100, blit=False)
    
    
    #animates a game of life with the start state listed as the 3rd uses updateM
    #parameter and in graph above
    aniM = animation.FuncAnimation(fig, animateM, [c0], 
                                   init_func=init, interval=100, blit=False)
    
    
    #plt.show()