import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
import datetime as dt

def stringToDatetime(string):
    if ("." in string):
        return dt.datetime.strptime(string, '%Y-%m-%d %H:%M:%S.%f UTC')
    else:
        return dt.datetime.strptime(string, '%Y-%m-%d %H:%M:%S UTC')

fields = ['timestamp', 'pixel_color', 'coordinate']
data = pd.read_csv('data/canvas.csv', usecols=fields, skipinitialspace=True)
print("Data loaded")

#frequency of coordinate use
print("Most popular pixels")
cF = data.coordinate.value_counts()
coordinateFrequency = pd.DataFrame({'coordinate':cF.index, 'frequency':cF.values})

ax = coordinateFrequency.head(20).plot.bar(x='coordinate', y='frequency', rot=0)

ax.set_xlabel('Pixel position')
ax.set_ylabel('Pixel updates')
ax.set_title('Most popular pixels')

ax.grid('on')

ax.spines['right'].set_color((.8,.8,.8))
ax.spines['top'].set_color((.8,.8,.8))

xlab = ax.xaxis.get_label()
ylab = ax.yaxis.get_label()

xlab.set_style('italic')
xlab.set_size(10)
ylab.set_style('italic')
ylab.set_size(10)

ttl = ax.title
ttl.set_weight('bold')

#frequency of color use
print("Most popular colors")
cF = data.pixel_color.value_counts()
colorFrequency = pd.DataFrame({'color':cF.index, 'frequency':cF.values})

ax = colorFrequency.head(16).plot.bar(x='color', y='frequency', rot=0)

ax.set_xlabel('Hex color code')
ax.set_ylabel('Color changes')
ax.set_title('Most popular colors')

ax.grid('on')

ax.spines['right'].set_color((.8,.8,.8))
ax.spines['top'].set_color((.8,.8,.8))

xlab = ax.xaxis.get_label()
ylab = ax.yaxis.get_label()

xlab.set_style('italic')
xlab.set_size(10)
ylab.set_style('italic')
ylab.set_size(10)

ttl = ax.title
ttl.set_weight('bold')

#activity chart
print("activity chart")
activity = data.timestamp
firstDate = stringToDatetime(activity.get(0))
templist = []

for i, value in activity.items():
        tmp = stringToDatetime(value)
        tmp = (tmp - firstDate).total_seconds()/60
        tmp = math.floor(tmp)
        templist.append(tmp)

activity = pd.DataFrame(templist)

a = activity[0].value_counts()

aF = pd.DataFrame({'minute':a.index, 'updates':a.values})
aF = aF.sort_values(by=['minute'], ascending=True)
ax = aF.plot(x='minute', y="updates")

l = ax.fill_between(aF.minute, aF.updates)

ax.set_xlabel('Minutes from first update')
ax.set_ylabel('Updates')
ax.set_title('Activity')
ax.grid('on')

l.set_facecolors([[.5,.5,.8,.3]])
l.set_edgecolors([[0, 0, .5, .3]])
l.set_linewidths([3])

ax.spines['right'].set_color((.8,.8,.8))
ax.spines['top'].set_color((.8,.8,.8))

xlab = ax.xaxis.get_label()
ylab = ax.yaxis.get_label()

xlab.set_style('italic')
xlab.set_size(10)
ylab.set_style('italic')
ylab.set_size(10)

ttl = ax.title
ttl.set_weight('bold')

print("SHOW")
plt.show()