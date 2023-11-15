list = eval(input("Enter the list items: "))
search = int(input("Enter the search item: "))
for i in range(0, len(list)):
    if search == list[i]:
        print(str(search) + " found at index: " + str(i))
        break
else:
    print(str(search) + " not present in the given list.")

