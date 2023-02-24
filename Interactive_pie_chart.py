# coding: utf-8
labels = ['Nokia', 'Samsung', 'Apple', 'Lumia']
values = [10, 30, 45, 15]
colors = ['yellow', 'green', 'red', 'blue']
explore = [0.3, 0, 0, 0]
plt.pie(values, labels=labels, colors=colors, explode=explode, shadow=true, autopct='%1.1f%%', startangele=180)
plt.pie(values, labels=labels, colors=colors, explode=explore, shadow=true, autopct='%1.1f%%', startangele=180)
plt.pie(values, labels=labels, colors=colors, explode=explore, shadow=True, autopct='%1.1f%%', startangele=180)
plt.pie(values, labels=labels, colors=colors, explode=explore, shadow=True, autopct='%1.1f%%', startangle=180)
plt.axis('equal')
plt.show()
get_ipython().run_line_magic('save', 'Interactive_pie_chart 49-59')
