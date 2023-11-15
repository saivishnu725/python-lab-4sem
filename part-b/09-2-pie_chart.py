import matplotlib.pyplot as plt

# data
names = ['a', 'b', 'c']
size = [40, 50, 10]
color = ['gold', 'red', 'blue', 'green']
explode = [0.1, 0, 0]

# plot the pie chart
plt.pie(size, labels=names, colors=color, shadow=True, explode=explode)

# title
plt.title("Pie Chart")

# display the chart
plt.show()

