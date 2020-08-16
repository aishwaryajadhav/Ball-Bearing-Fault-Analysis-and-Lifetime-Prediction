# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 21:21:22 2017

@author: Dell
"""

from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.spatial.distance import pdist 
import numpy as np
import pandas
#names1 = ['A','B']
#dataset2 = pandas.read_csv('C:\\Users\\Dell\\Downloads\\denoised1.csv',names=names1)

#A2 = dataset2['A'][:2400]
#B2 = dataset2['B'][:2400]
names2 = ['A','B','C','D','E','F','G']
dataset3 = pandas.read_csv('C:\\Users\\Dell\\Downloads\\test1.csv',names=names2)
A3 = dataset3['A'][:1000]
B3 = dataset3['B'][:1000]
C3 = dataset3['C'][:1000]
D3 = dataset3['D'][:1000]
E3 = dataset3['E'][:1000]
F3 = dataset3['F'][:1000]
G3 = dataset3['G'][:1000]


#combined1= np.vstack((A2,B2)).T
combined1= np.vstack((A3,B3,C3,D3,E3,F3,G3)).T
y = pdist(combined1,'euclidean')
z=linkage(y,'single')
#print z
plt.figure(figsize=(50, 10))
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('sample index')
plt.ylabel('distance')
R=dendrogram(z,leaf_font_size=12)
plt.show()
#print R['ivl']

