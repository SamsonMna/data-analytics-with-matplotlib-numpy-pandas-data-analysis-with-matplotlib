# coding: utf-8
from sklearn.decomposition import PCA
x_reduced = PCA(n_components=3).fit_transform(iris.data)
iris = datasets.load_iris()
species = iris.target #Species
from mpl_toolkits.mplot3d import Axes3D
#Scatterplot
fig = plt.figure()
ax = Axes3D(fig)
ax.set_title("Iris Dataset by PCA", size=14)
ax.scatter(x_reduced[:, 0], x_reduced[:, 1]. x_reduced[:, 2], c=species)
ax.scatter(x_reduced[:, 0], x_reduced[:, 1], x_reduced[:, 2], c=species)
ax.set_xlabel('First eigenvector')
ax.set_ylabel('Second eigenvector')
ax.set_zlabel('Third eigenvector')
ax.w_xaxis.set_ticklabels(())
ax.w_yaxis.set_ticklabels(())
ax.xaxis.set_ticklabels(())
