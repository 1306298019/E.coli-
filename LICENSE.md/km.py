from scipy.cluster.vq import *  
import numpy as np   
import time  
import matplotlib.pyplot as plt  
  
## step 1: load data  
print "step 1: load data..."  
dataSet = []  
fileIn = open('D:/python/jvlei.txt')  
for line in fileIn.readlines():  
    lineArr = line.strip().split('\t')  
    dataSet.append([float(lineArr[0]), float(lineArr[1])])  
  
## step 2: clustering...  
print "step 2: clustering..."  
dataSet =np.mat(dataSet)  
k = 4  
centroids, clusterAssment = kmeans(dataSet, k)  
code,distance=vq(dataSet,centroids) 

## step 3: show the result  
plt.figure()  
ndx=np.where(code==3)[0]  
plt.plot(dataSet[ndx,0],dataSet[ndx,1],'*')  
ndx=np.where(code==2)[0]  
plt.plot(dataSet[ndx,0],dataSet[ndx,1],'o')  
ndx=np.where(code==1)[0]  
plt.plot(dataSet[ndx,0],dataSet[ndx,1],'1')  
ndx=np.where(code==0)[0]  
plt.plot(dataSet[ndx,0],dataSet[ndx,1],'r.')  
plt.plot(centroids[:,0],centroids[:,1],'go')  
plt.axis('off')  
plt.show()  