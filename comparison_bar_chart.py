# coding: utf-8
x0 =  np.arange(8)
y1 = np.array([1,3,4,6,3,2,1])
y2 = np.array([1,2,5,4,3,3,2,1])
y1 = np.array([1,3,4,6,4,3,2,1])
plt.ylim(-7, 7)
plt.bar(x0, y1, 0.9, facecolor='r')
plt.bar(x0, -y2, 0.9, facecolor='b')
plt.xticks(())
plt.grid(True)
for x, y in zip(x0, y1):
    plt.text(x + 0.4, y +0.05, '%d' % y, ha='center', va='bottom')
    
for x, y in zip(x0, y2):
    plt.text(x + 0.4, -y - 0.05, '%d' % y, ha='center', va='top')
    
plt.show()
