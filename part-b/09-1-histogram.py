import matplotlib.pyplot as plt

# data
toys = [4, 3, 7, 2, 5, 7, 7, 1, 2, 8, 8, 7, 6, 3, 2, 1]

# plot the histogram
plt.hist(toys, bins=range(0, 10), edgecolor='black')

# title
plt.xlabel("Toys")
plt.ylabel("Kids")
plt.title("Histogram")

# display the histogram
plt.show()

