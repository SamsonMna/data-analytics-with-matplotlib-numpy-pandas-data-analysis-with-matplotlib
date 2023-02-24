# coding: utf-8
# %load scatterplot_for_iris_dataset.py
import matplotlib.patches as mpatches
x = iris.data[:,2] #X_Axis petal length
y = iris.data[:,3] #Y_Axis petal length
species = iris.target #Species
x_min, x_max = x.min() - .5, x.max() + .5
y_min, y_max = y.min() - .5, y.max() + .5
#Scatterplot
plt.figure()
plt.title('Iris Dataset - Classification by Petal sizes', size=14)
plt.scatter(x, y, c=species)
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.ylim(y_min, y_max)
plt.xticks(())
plt.yticks(())
