# coding: utf-8
# %load k-nearest-neighbor-classifier.py
get_ipython().run_line_magic('run', 'imports.py')
import matplotlib.patches as mpatches
from sklearn.neighbors import KNeighborsClassifier
from sklearn import datasets
from matplotlib.colors import ListedColormap
iris = datasets.load_iris()
x = iris.data[:,2:4] #X-Axis Petal length-width
y = iris.target
x_min, x_max = x[:,0].min() - .5, x[:,0].max() + .5
y_min, y_max = x[:,1].min() - .5, x[:,1].max() + .5
#MESH
cmap_light = ListedColormap(['#AAAAFF', '#AAFFAA', '#FFAAAA'])
knn = KNeighborsClassifier()
knn.fit(x,y)
h = .02
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
Z = knn.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
plt.figure()
plt.pcolormesh(xx, yy, Z, cmap=cmap_light)
# Plot the training points
plt.scatter(x[:,0], x[:,1], c=y)
plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())
