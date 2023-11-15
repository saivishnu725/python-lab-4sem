import numpy as np

# create two arrays
a1 = np.array([1, 2, 3, 20, 50, 3, 6, 3])
a2 = np.array([12, 12, 1, 50, 20, 10, 20, 10])

# subtract
print("Subtraction: ", np.subtract(a1, a2))

# add 
print("Addition: ", np.add(a1, a2))

# multiply
print("Multiply: ", np.multiply(a1, a2))

# divide
print("Division: ", np.divide(a1, a2))


## Logical operations
# logical and
print("Logical and: ", np.logical_and(a1, a2))
# logical or 
print("Logical or: ", np.logical_or(a1, a2))
# logical and
print("Logical not: ", np.logical_not(a1))

## aggregate functions

print("Sum of a1: ", np.sum(a1))
print("Max of a1: ", np.max(a1))
print("Min of a1: ", np.min(a1))
print("Average of a1: ", np.average(a1))

## statistical operations
print("Mean of a1: ",np.mean(a1))
print("Mode: ", np.mod(a1, a2))
print("Median: ", np.median(a1))
print("Sort a2: ", np.sort(a2))

