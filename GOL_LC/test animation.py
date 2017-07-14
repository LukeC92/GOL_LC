"""
A simple example of an animated plot
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

x = np.arange(0, 2*np.pi, 0.01)
line, = ax.plot(x, np.sin(x))


def animate(data):
    data[...] = np.roll(data, 1)
    line.set_ydata(np.sin(x + data[0]/10.0))
    return line,


# Init only required for blitting to give a clean slate.
def init():
    line.set_ydata(np.ma.array(x, mask=True))
    return line,

data = [np.arange(1, 200)]
ani = animation.FuncAnimation(fig, animate, data, init_func=init,
                              interval=25, blit=True)
plt.show()
