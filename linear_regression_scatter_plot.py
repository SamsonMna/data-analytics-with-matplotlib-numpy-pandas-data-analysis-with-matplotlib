# coding: utf-8
from sklearn import linear_model
linreg = linear_model.linearRegression()
linreg = linear_model.LinearRegression()
x_train = diabetes.data[:-20]
y_train = diabetes.target[:-20]
x_test = diabetes.data[-20:]
y_test = diabetes.target[-20:]
linreg.fit(x_train, y_train)
linreg.coef_
linreg.predict(x_test)
y_test
linreg.score(x_test, y_test)
x0_test = x_test[:,0]
x0_train = x_train[:,0]
x0_test = x0_test[:, np.newaxis]
x0_train = x0_train_[:, np.newaxis]
x0_train = x0_train[:, np.newaxis]
linreg = linear_model.LinearRegression()
linreg.fit(x_train, y_train)
y = linreg.predict(x0_test)
linreg.fit(x0_train, y_train)
y = linreg.predict(x0_test)
plt.scatter(x0_test, y_test, color='k')
plt.plot(x0_test, y, color='b', linewidth=3)
