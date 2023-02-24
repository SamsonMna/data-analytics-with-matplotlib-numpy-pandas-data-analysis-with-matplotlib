# coding: utf-8
n = 8
theta = np.arange(0., 2* np.pi, 2 * np.pi / n)
radii = np.array([4,7,5,3,1,5,6,7])
plt.axes([0.025, 0.025, 0.95, 0.95], polar=True)
colors = np.array(['#4bb2c5', '#c5b47f', '#EAA228', '#579575', '#839557', '#958c12', '#953579', '#4b5de4'])
bars = plt.bar(theta, radii, width=(2*np.pi/n), bottom=0.0, colors=colors)
bars = plt.bar(theta, radii, width=(2*np.pi/n), bottom=0.0, color=colors)
plt.show()
