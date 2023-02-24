# coding: utf-8
data = {'series1': [1,3,4,3,5], 'series2': [2,4,5,2,4], 'series3': [3,2,3,1,3]}
df = pd.DataFrame(data)
df.plot(kind='barh')
plt.show()
