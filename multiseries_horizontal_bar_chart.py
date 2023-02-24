# coding: utf-8
index = np.arange(5)
values1 = [5, 7, 3, 4, 6]
values2 = [6, 6, 4, 5, 7]
values3 = [5, 6, 5, 4, 6]
bw = 0.3
plt.axis([0, 8, 0, 5])
plt.title("A multiseries Horizontal Bar Chart", fontsize=20)
plt.barh(index, values1, bw, color='b')
plt.barh(index+bw, values2, bw, color='g')
plt.barh(indx+2*bw, values3, bw, color='r')
plt.barh(index+2*bw, values3, bw, color='r')
plt.yticks(index+0.4, ['A', 'B', 'C', 'D', 'E'])
plt.show()
