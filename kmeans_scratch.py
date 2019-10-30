# KMeans Clustering (Flat Clustering)

import matplotlib.pyplot as plt
import numpy as np

X = np.array([[1,2],
             [1.5,1.8],
             [5,8],
             [8,8],
             [1,0.6],
             [9,11]])


plt.scatter(X[:,0], X[:,1], s=150)
plt.show()

colors = 10*["g.","r.","c.","b.","k.","o."]