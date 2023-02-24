# coding: utf-8
for f in range(0, 10):
    xi_test = x_test[:, f]
    xi_train = x_train[:, f]
    xi_test = xi_test[:, np.newaxis]
    xi_train= xi_train[:, np.newaxis]
    linreg.fit(xi_train, y_train)
    
Y = linreg.predict(xi_test)
plt.subplot(5,2, f+1)
plt.scatter(xi_test, y_test, color='k')
plt.plot(xi_test, y, color='b', linewidth=3)
plt.show()
for f in range(0, 10):
    xi_test = x_test[:, f]
    xi_train = x_train[:, f]
    xi_test = xi_test[:, np.newaxis]
    xi_train= xi_train[:, np.newaxis]
    linreg.fit(xi_train, y_train)
for f in range(0, 10):
    xi_test = x_test[:, f]
    xi_train = x_train[:, f]
    xi_test = xi_test[:, np.newaxis]
    xi_train= xi_train[:, np.newaxis]
    
ligreg.fit(xi_train, y_train)
linreg.fit(xi_train, y_train)
Y = linreg.predict(xi_test)
plt.subplot(5,2, f+1)
plt.scatter(xi_test, y_test, color='k')
plt.plot(xi_test, y, color='b', linewidth=3)
plt.show()
for f in range(0, 10):
    xi_test = x_test[:, f]
    xi_train = x_train[:, f]
    xi_test = xi_test[:, np.newaxis]
    xi_train= xi_train[:, np.newaxis]
    linreg.fit(xi_train, y_train)
    Y = linreg.predict(xi_test)
    plt.subplot(5, 2, f+1)
    plt.scatter(xi_test, y_test, color='k')
    plt.plot(xi_test, y, color='b', linewidth=3)
    
