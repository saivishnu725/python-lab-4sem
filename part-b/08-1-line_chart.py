import matplotlib.pyplot as plt

# data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

#plot the line chart
plt.plot(x, y, marker='o', linestyle="-", color='blue')
plt.title("Line chart")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.grid(True)
plt.show()

