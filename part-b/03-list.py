l1 = [10, 20, 30]

# print the entire list
print("Entire List: ", l1)

# access an item using index
print("Item at index 2: ", l1[2])

# change/update item using index
l1[0] = 100
print("Updated List: ", l1)

# length of the list
print("Length: ", len(l1))

# max and min
print("Maximum: ", max(l1))
print("Minimum: ", min(l1))


## list operations
# concatenation
l2 = [80, 90, 100]
print("Concatentation: ", (l1 + l2))

# repetition
print("Repetition: ", (l1 * 2))

# slicing
print("Sliced List: ", (l1[0:2]))

# membership
print("100 in List: ", (100 in l1))
print("100 not in List: " ,(100 not in l1))


## manipulation operations
# append()
l1.append(50.5)
print("List after append: ", l1)

# pop()
print("Popped item: ", l1.pop())
print("List after pop: ", l1)

# insert()
l1.insert(4, 40)
print("List after insert: ", l1)

# extend()
l1.extend([60, 50])
print("List after extend: ", l1)

# sort()
l1.sort()
print("Sorted List:", l1)

# reverse()
l1.reverse()
print("Reversed List", l1)

