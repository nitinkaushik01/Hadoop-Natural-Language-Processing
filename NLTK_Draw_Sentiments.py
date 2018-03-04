# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 11:39:03 2018

@author: Nitin
"""

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

style.use("ggplot")

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    pullData = open ("F:/output.txt", "r").read()
    lines = pullData.split('\n')
    
    xar = []
    yar = []
    
    x = 0
    y = 0
    
    for l in lines[-100:]:
        x+=1
        if "positive" in l:
            y+=1
        elif "negative" in l:
            y -= 1
            
        xar.append(x)
        yar.append(y)
    ax1.clear()
    ax1.plot(xar, yar)
    
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()













