import GOL_LC




import numpy as np
import matplotlib.pyplot as plt

blip = np.zeros((5,5))
blip[1,2] = 1
blip[2,2] = 1
blip[3,2] = 1

#print("hello")
#print(blip)
#plt.pcolormesh(blip, cmap='Greys')
#plt.grid(color='black')
#plt.show()

print(blip)
print(GOL_LC.alive(1, 2, blip))
    
#want to take the numbers from sumcells and build a new array filled with 1s and 0s depending on the values of sumcells
    