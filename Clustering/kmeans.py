import matplotlib.pyplot as plt
import pandas
import numpy as np
from scipy import cluster

np.set_printoptions(threshold=np.inf)
names = ['A','B','C','D']
names2 = ['A','B','C','D','E','F','G','H','I']
names1 = ['A','B']

dataset1 = pandas.read csv('C:\\Users\\Dell\\Downloads\\testxy pca.csv',names=names)
dataset2 = pandas.read csv('C:\\Users\\Dell\\Downloads\\denoised.csv',names=names1)
dataset3 = pandas.read csv('C:\\Users\\Dell\\Downloads\\testxy wpca.csv',names=names2)
count=1024
A1 = dataset1['A'][:1024]
B1 = dataset1['B'][:1024]
C1 = dataset1['C'][:1024]
D1 = dataset1['D'][:1024]
A3 = dataset3['A'][:1024]
B3 = dataset3['B'][:1024]
C3 = dataset3['C'][:1024]
D3 = dataset3['D'][:1024]
E3 = dataset3['E'][:1024]
F3 = dataset3['F'][:1024]
G3 = dataset3['G'][:1024]
H3 = dataset3['H'][:1024]
I3 = dataset3['I'][:1024]
A2 = dataset2['A'][:102400]
B2 = dataset2['B'][:102400]

combined= np.vstack((A1,B1,C1,D1)).T
combined2= np.vstack((A3,B3,C3,D3,E3,F3,G3,H3,I3)).T
combined1= np.vstack((A2,B2)).T

initial2 = [cluster.vq.kmeans(combined2,i) for i in range(1,10)]
initial1 = [cluster.vq.kmeans(combined1,i) for i in range(1,10)]

plt.plot([var1 for (cent1,var1) in initial1])
plt.show()

initial = [cluster.vq.kmeans(combined,i) for i in range(1,10)]
plt.plot([var for (cent,var) in initial])
plt.show()

cent, var = initial[1]
cent1, var1 = initial1[1]
cent2, var2 = initial2[1]

print "The denoised cost is "
print var1
print "The after-pca cost is "
print var
print "The bfr-pca cost is "
print var2
#print cent
#use vq() to get as assignment for each obs.
assignment,cdist = cluster.vq.vq(combined,cent)
assignment1,cdist1 = cluster.vq.vq(combined1,cent1)
assignment2,cdist2 = cluster.vq.vq(combined2,cent2)
#print assignment
plt.scatter(combined1[:,0], combined1[:,1], c=assignment1)
plt.show()