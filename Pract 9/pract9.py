print("Shardul Prabhu")
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
a,b = make_blobs(n_samples=300, centers=4,cluster_std=0.60,random_state=0)
plt.scatter(a[:,0],a[:,1])
plt.title('Shardul')
plt.show()
wcss = []
for i in range(1, 11):
    kmean = KMeans(n_clusters=i, init='k-means++',max_iter=300, n_init=10,random_state=0)
    kmean.fit(a)
    wcss.append(kmean.inertia_)
plt.plot(range(1,11),wcss)
plt.title('Elbow method')
plt.xlabel("Number of cluster")
plt.ylabel("wcss")
plt.show()
kmean = KMeans(n_clusters=4, init='k-means++',max_iter=300, n_init=10,random_state=0)
pred_b = kmean.fit_predict(a)
plt.scatter(a[:,0],a[:,1])
plt.scatter(kmean.cluster_centers_[:,0], kmean.cluster_centers_[:,1], s=300, c='red')
plt.show()
