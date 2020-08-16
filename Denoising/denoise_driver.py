import matplotlib
from pandas.tools.plotting import scatter matrix
import matplotlib.pyplot as plt
import scipy.io
import pandas
import math
import matplotlib.lines as mlines
import numpy as np
import scipy.stats as sta
from savitzky_golay_filter import *
from moving_average import *

names = ['A','B']
dataset1 = pandas.read csv('C:\\Users\\Dell\\Downloads\\original.csv',names=names)
count=2500
A1 = dataset1['A'][:count]
B1 = dataset1['B'][:count]
print sta.signaltonoise(A1)
print sta.signaltonoise(B1)
s1=savitzky_golay(A1,11,3)
s2=savitzky_golay(B1,11,3)
print sta.signaltonoise(s1)
print sta.signaltonoise(s2)
plt.show()
plt.figure()
plt.plot(A1)
plt.plot(s1,'red')

blue line = mlines.Line2D([], [], color='blue', label='Initial Plot')
red line = mlines.Line2D([], [], color='red', label='Smoothed Plot')

plt.legend(handles=[blue line,red line])
plt.figure()
plt.plot(B1)
plt.plot(s2,'green')
blue line = mlines.Line2D([], [], color='blue', label='Initial Plot')
red line = mlines.Line2D([], [], color='green', label='Smoothed Plot')

plt.legend(handles=[blue line,red line])

yMA = movingaverage(B1,10)
xMA = movingaverage(A1,10)
plt.show()
plt.plot(yMA,"green")
plt.show()
plt.plot(xMA,"red")