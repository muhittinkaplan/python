import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import PathCollection

xVal=np.arange(0,5)
yVal=np.random.randint(0,100,5)
strVal=np.array(['1881','1919','1920','1923','1938'])
fig, ax = plt.subplots()
coll = ax.scatter(xVal,yVal, picker = 5)
box=[]

def on_key(event):
    for i in box:
        i.remove()
    box.clear()
    fig.canvas.draw()

def on_pick(event):
    print("Mouse x:{} y:{} button:{}".format(event.mouseevent.xdata,event.mouseevent.ydata,event.mouseevent.button))
    if(isinstance(event.artist,PathCollection)):

        print (xVal[event.ind], "clicked")
        dataCursorTextVal=strVal[event.ind][0]
        dataCursorLocation=event.mouseevent.xdata+0.5,event.mouseevent.ydata+0.5
        dataCursorTargetLocation=event.mouseevent.xdata,event.mouseevent.ydata
        z=plt.annotate(dataCursorTextVal,dataCursorTargetLocation, dataCursorLocation, 'data',
                         arrowprops=dict(arrowstyle="-|>", connectionstyle="arc3,rad=0.3",
                                         lw=1,edgecolor='black'),
                         bbox=dict(facecolor='yellow', edgecolor='black',boxstyle='round,pad=0.5',alpha=0.5),
                         size=6, ha="center")

        box.append(z)
        box[box.__len__()-1].draggable()
        fig.canvas.draw()

fig.canvas.mpl_connect('pick_event', on_pick)
cid = fig.canvas.mpl_connect('key_press_event', on_key)
plt.show()
