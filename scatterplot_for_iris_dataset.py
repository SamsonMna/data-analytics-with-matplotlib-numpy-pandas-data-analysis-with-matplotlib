# coding: utf-8
import matplotlib.patches as mpatches
x = iris.data[:,0] #X_Axis -sepal length
y = iris.data[:,1] #Y_Axis sepal length
species = iris.target #Species
x_min, x_max = x.min() - .5, x.max() + .5
y_min, y_max = y.min() - .5, y.max() + .5
#Scatterplot
plt.figure()
plt.title('Iris Dataset - Classification by Sepal sizes')
plt.scatter(x, y, c=species)
plt.xlabel('Sepal Length')
plt.ylabel('Sepal width')
plt.xlim(x_min, x_max)
ply.ylim(y_min, y_max)
plt.ylim(y_min, y_max)
plt.xticks(())
plt.yticks(())
plt.show()
