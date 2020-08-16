import scipy.io
import pandas
import math
import numpy as np
import csv
from sklearn.decomposition import PCA

names = ['A','B','C','D','E','F','G','H','I']
dataset1 = pandas.read csv('C:\\Users\\Dell\\Downloads\\test1.csv',names=names)
pca = PCA(n components=4)
new features = pca.fit(dataset1).transform(dataset1)
print pca.explained variance ratio .cumsum()

with open('testxy_pca.csv', 'wb') as f:
    wtr = csv.writer(f, delimiter= ',')
    wtr.writerows(new features)