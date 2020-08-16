import scipy.io
import pandas
import math
import numpy as np
from sklearn.decomposition import PCA
import csv


names = ['A','B']
dataset1 = pandas.read csv('C:\\Users\\Dell\\Downloads\\denoised.csv',names=names)
count=102401

s1 = dataset1['A'][:count]
s2 = dataset1['B'][:count]

rms=[]
stddev=[]
peak=[]
kur=[]
skew=[]
crest=[]
clf=[]
impulse=[]
shp=[]

rms_b=[]
stddev_b=[]
peak_b=[]
kur_b=[]
skew_b=[]
crest_b=[]
clf_b=[]
impulse_b=[]
shp_b=[]

for i in range(0, np.shape(s1)[0]):
    if i%100==0:
        if(i+100<np.shape(s1)[0]):
            en=i+100
        else:
            en=np.shape(s1)[0]
        a=np.square(s1[i:en])
        a=np.mean(a, axis=0)
        r=np.sqrt(a)
        rms.append(r)
        s=np.std(s1[i:en], axis=0)
        stddev.append(s)
        peak.append(np.max(s1[i:en])-np.min(s1[i:en]))
        a=np.mean(s1[i:en])
        a=s1[i:en]-a
        b=np.power(a,4)
        b=np.mean(b,axis=0)
        kur.append(b/np.power(s,4))
        b=np.power(a,3)
        b=np.mean(b,axis=0)
        skew.append(b/np.power(s,3))
        ma=np.max(s1[i:en])
        crest.append(ma/r)
        ab=np.abs(s1[i:en])
        a=np.mean(ab,axis=0)
        impulse.append(ma/a)
        b=np.sqrt(ab)
        b=np.mean(b,axis=0)
        clf.append(ma/np.square(b))
        shp.append(r/a)
        a=np.square(s2[i:en])
        a=np.mean(a, axis=0)
        r=np.sqrt(a)
        rms b.append(r)
        s=np.std(s2[i:en], axis=0)
        stddev b.append(s)
        peak b.append(np.max(s2[i:en])-np.min(s2[i:en]))
        a=np.mean(s2[i:en])
        a=s2[i:en]-a
        b=np.power(a,4)
        b=np.mean(b,axis=0)
        kur b.append(b/np.power(s,4))
        b=np.power(a,3)
        b=np.mean(b,axis=0)
        skew b.append(b/np.power(s,3))
        ma=np.max(s2[i:en])
        crest b.append(ma/r)
        ab=np.abs(s2[i:en])
        a=np.mean(ab,axis=0)
        impulse b.append(ma/a)
        b=np.sqrt(ab)
        b=np.mean(b,axis=0)
        clf b.append(ma/np.square(b))
        shp b.append(r/a)
        i=i+99


rms = np.array(rms, dtype=np.float64)
stddev = np.array(stddev, dtype=np.float64)
peak = np.array(peak, dtype=np.float64)
kur = np.array(kur, dtype=np.float64)
skew = np.array(skew, dtype=np.float64)
crest = np.array(crest, dtype=np.float64)
clf = np.array(clf, dtype=np.float64)
impulse = np.array(impulse, dtype=np.float64)
shp = np.array(shp, dtype=np.float64)
rms_b = np.array(rms_b, dtype=np.float64)
stddev_b = np.array(stddev_b, dtype=np.float64)
peak_b = np.array(peak_b, dtype=np.float64)
kur_b = np.array(kur_b, dtype=np.float64)
skew_b = np.array(skew_b, dtype=np.float64)
crest_b = np.array(crest_b, dtype=np.float64)
clf_b = np.array(clf_b, dtype=np.float64)
impulse_b = np.array(impulse_b, dtype=np.float64)
shp_b = np.array(shp_b, dtype=np.float64)

feature=[]
feature.append(rms)
feature.append(stddev)
feature.append(peak)
feature.append(kur)
feature.append(skew)
feature.append(clf)
feature.append(impulse)
feature.append(shp)
feature.append(crest)
feature.append(rms_b)
feature.append(stddev_b)
feature.append(peak_b)
feature.append(kur_b)
feature.append(skew_b)
feature.append(crest_b)
feature.append(clf_b)
feature.append(impulse_b)
feature.append(shp_b)
feature = np.array(feature, dtype=np.float64)
feature=np.transpose(feature)

with open('test wpca.csv', 'wb') as f:
    wtr = csv.writer(f, delimiter= ',')
    wtr.writerows(feature)
