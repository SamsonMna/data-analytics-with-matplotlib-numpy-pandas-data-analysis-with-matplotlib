# coding: utf-8
iris = datasets.load_iris()
x = iris.data[:, :2]
y = iris.target
h = .02
h = .05
svc = svm.SVC(kernel='linear', C=1.0).fit(x,y)
x_min, x_max = x[:,0].min() - .5, x[:,0].max() + .5
y_min, y_max = x[:,1].min() - .5, x[:,1].max() + .5
h = .02
X, Y = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
Z = svc.predict(np.c_[X.ravel(), Y.ravel()])
Z = Z.reshape(X.shape)
plt.contourf(X,Y,Z, alpha=0.4)
plt.contour(X,Y,Z, colors='k')
plt.scatter(x[:, 0], x[:,1], c=y)
