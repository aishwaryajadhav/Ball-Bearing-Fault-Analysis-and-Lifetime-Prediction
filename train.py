import pickle
from sklearn.cluster import KMeans
#import scipy.io
import matplotlib.pyplot as plt
from scipy import cluster
import pandas
#import math
import numpy as np
from sklearn.decomposition import PCA

def build build_gaussian_filter_1d filter 1d(n,s,N):
    x = ( np.arange(n)-(n-1)/2 )/(N-1)
    f = np.exp( - x**2 /(2 * (s**2)) )
    f = f / f.sum()
    return f

def my_pca(comp, X1):
    X=X1
    m=np.mean(X,axis=0)
    X=X-m
    s=np.std(X,axis=0)
    X=X/s
    cov=(np.matmul(np.transpose(X),X))/np.shape(X)[0]
    u,s,v = np.linalg.svd(cov, full matrices=True)
    feat=np.matmul(X,u[:,0:comp])
    return feat

names = ['A','B']
dataset1 = pandas.read csv('C:\\Users\\meais\\Desktop\\sem 6\\Labs\\nML\\original.csv',names=names)

c=dataset1.A.count()
count=int(c*60/100)
#training set
A1 = dataset1['A'][:count]
B1 = dataset1['B'][:count]
#cv set
count1=int(c*20/100)
A_cv=dataset1['A'][count:(count1+count)]
B_cv=dataset1['B'][count:(count1+count)]
#test set
A_test=dataset1['A'][(count1+count):2*count1+count]
B_test=dataset1['B'][count1+count:2*count1+count]
f=build_gaussian_filter_1d(3,2,count)
#Training set
pca = PCA()
feat = pca.fit transform(feature)
pkl_pca = open("C:\\Users\\meais\\Desktop\\sem 6\\Labs\\nML\\bearing.pca","wb" )
pickle.dump(pca, pkl_pca)
pkl_pca.close()
feature=feature[:,0:6]
kmeans = KMeans(n clusters=2, random state=0).fit(feature)
pkl_model= open("C:\\Users\\meais\\Desktop\\sem 6\\Labs\\nML\\bearing.model","wb" )
pickle.dump(kmeans, pkl_model)
pkl_model.close()

#On test set
s1=np.convolve( f[::-1], A_cv, mode='valid')
s2=np.convolve( f[::-1], B_cv, mode='valid')
feature=get features(s1,s2)
feat = pca.transform(feature)
feature cv=feat[:,0:6]
kmeans.predict(feature cv)
#Calculating scores on training and cv set
print(kmeans.score(feature)/np.shape(feature)[0])
print(kmeans.score(feature cv)/np.shape(feature cv)[0])