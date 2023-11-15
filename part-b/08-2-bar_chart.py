import matplotlib.pyplot as plt

# data
user = ['a', 'b', 'c']
marks = [20, 50, 80]

# plot the bar chart
plt.bar(user, marks, width=0.8, color='blue', edgecolor='red')

# title
plt.xlabel("Users")
plt.ylabel('Marks')
plt.title("Bar Chart")

# display the chart
plt.show()

