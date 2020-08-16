import pandas
import math
import matplotlib.lines as mlines
import numpy as np
import scipy
import matplotlib
from pandas.tools.plotting import scatter matrix
import matplotlib.pyplot as plt
import scipy.io

def build_gaussian_filter_1d(n,s,N):
    x = ( np.arange(n)-(n-1)/2 )/(N-1)
    f = np.exp( - x**2 /(2 * (s**2)) )
    f = f / f.sum()
    return f


names = ['A','B']
dataset1 = pandas.read csv('C:\\Users\\Dell\\Downloads\\original.csv',names=names)
count=2501
A1 = dataset1['A'][7500:10001]
B1 = dataset1['B'][7500:10001]
print sta.signaltonoise(A1)
print sta.signaltonoise(B1)
f=build_gaussian_filter_1d(11,2,2501)
s1=np.convolve( f[::-1], A1, mode='valid')
s2=np.convolve( f[::-1], B1, mode='valid')
comb=np.vstack((s1,s2)).T
with open('denoised1.csv', 'wb') as f:
    wtr = csv.writer(f, delimiter= ',')
    wtr.writerows(comb)
print sta.signaltonoise(s1)
print sta.signaltonoise(s2)
plt.show()
plt.figure()
plt.plot(A1)
plt.plot(s1,'red')
blue line = mlines.Line2D([], [], color='blue', label='Initial VerAcc')
red line = mlines.Line2D([], [], color='red', label='Smoothed')
plt.legend(handles=[blue line,red line])
plt.figure()
plt.plot(B1)
plt.plot(s2,'green')
blue line = mlines.Line2D([], [], color='blue', label='Initial HorAcc')
red line = mlines.Line2D([], [], color='green', label='Smoothed')
plt.legend(handles=[blue line,red line])