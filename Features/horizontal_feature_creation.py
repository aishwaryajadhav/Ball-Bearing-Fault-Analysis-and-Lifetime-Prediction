import scipy.io
import pandas
import math
import numpy as np
import csv
from sklearn.decomposition import PCA

names = ['A','B']
dataset1 = pandas.read csv('C:nnUsersnnDellnnDownloadsnndenoised.csv',names=names)
count=5001

s1 = dataset1['A'][:count]
s2 = dataset1['B'][:count]

feature=np.vstack((s1,s2))
a=np.square(feature)
a=np.mean(a, axis=0)
rms=np.sqrt(a)
standdev=np.std(feature, axis=0)
peak=np.abs(feature[0,:]-feature[1,:])
ma=np.max(feature,axis=0)
crest=ma/rms
ab=np.abs(feature)
a=np.mean(ab,axis=0)
impulse=ma/a
b=np.sqrt(ab)
b=np.mean(b,axis=0)
clf=ma/np.square(b)
shape=rms/a
feature=np.vstack((feature,rms))
feature=np.vstack((feature,standdev))
feature=np.vstack((feature,peak))
feature=np.vstack((feature,crest))
feature=np.vstack((feature,impulse))
feature=np.vstack((feature,clf))
feature=np.vstack((feature,shape))
feature=np.transpose(feature)

with open('testxy wpca.csv', 'wb') as f:
    wtr = csv.writer(f, delimiter= ',')
    wtr.writerows(feature)