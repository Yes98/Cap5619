import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random
fig, ax = plt.subplots()
x0,y0, h0 = np.random.randint(-17,17,size=(100,)),np.random.randint(-17,17,size=(100,)),np.random.randint(1,360,size=(100))
figs = []

scat = ax.scatter(x0,y0)
x1,y1, h1 = np.random.randint(-17,17,size=(100,)),np.random.randint(-17,17,size=(100,)),np.random.randint(1,360,size=(100))
#scat= ax.scatter(x1,y1)
def animate(i):
    print(i)
    fig.clear()
    x1,y1, h1 = np.random.randint(-17,17,size=(100,)),np.random.randint(-17,17,size=(100,)),np.random.randint(1,360,size=(100))
    scat = ax.scatter(x1,y1)
anim = FuncAnimation(fig, animate,frames = 20, interval=700)
plt.draw()
plt.show()
