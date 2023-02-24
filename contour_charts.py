# coding: utf-8
dx = 0.01; dy = 0.01
x = np.arange(-2.0, 2.0, dx)
y = np.arange(-2.0, 2.0, dy)
X,Y np.meshgrid(x, y)
X,Y = np.meshgrid(x, y)
def f(x, y):
    return (1 - y**5 + x**5)*np.exp(-x**2-y**2)
    
c = plt.contour(X, Y, f(X, Y), 8, colors='black')
plt.contour(X, Y, f(X, Y), 8)
plt.clabel(c, inline=1, fontsize=10)
plt.show()
dx = 0.01; dy = 0.01
x = np.arange(-2.0, 2.0, dx)
y = np.arange(-2.0, 2.0, dy)
X,Y = np.meshgrid(x, y)
def f(x, y):
    return (1 - y**5 + x**5)*np.exp(-x**2-y**2)
    
c = plt.contour(X, Y, f(X, Y), 8, colors='black')
plt.contourf(X,Y, f(X,Y),8,cmap=plt.cm.hot)
plt.clabel(c, inline=1, fontsize=10)
plt.colorbar()
plt.show()
