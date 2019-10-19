import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")
from sklearn.cluster import KMeans
from sklearn.preprocessing import scale

df = pd.read_csv(r"Amazon Book Analysis/Filtered Data.tsv", delimiter='\t')
print(df.size)
df.drop_duplicates(subset='Title',keep='last',inplace = True)
df = df.dropna()
df = df.set_index('Title')
array = df.to_numpy()

""" x = np.delete(array, [0,1,3], axis =1)
y = np.delete(array, [0,2,3], axis =1)

plt.scatter(x,y)
plt.show() """

X = np.delete(array, [0,3], axis=1)
X = X.astype(np.float)
X = scale( X, axis=0, with_mean=True, with_std=True, copy=True)

#setting up model and training
kmeans = KMeans(n_clusters=3)
kmeans.fit(X)

#visualizing data, centroid = the center point of clusters
#KMeans assigns labels to things based on cluster
centroids = kmeans.cluster_centers_
labels = kmeans.labels_
print(centroids)
print(labels)

#futher visualising || _ means worthless variable
colors = ["g.","r.","y."]
for _ in range(len(X)):
    print("coordinate:",X[_], "label:", labels[_])
    plt.plot(X[_][0], X[_][1], colors[labels[_]], markersize = 10)

plt.scatter(centroids[:, 0],centroids[:, 1], marker = "x", s=150, linewidths = 5, zorder = 10)
plt.show()
