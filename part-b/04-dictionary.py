d = {
        "name": "abc",
        "roll": 123,
        "branch": "cse",
        "phone": 1234567890
}

print("Entire Dictionary: ", d)

# length of the dictionary
print("Length of Dictionary:", len(d))

# append to the end of the dictionary
d["fee"] = 1000
print("Dictionary after append: ", d)

# change/update an item in dictionary
d["fee"] = 2000
print("Dictionary after updating an item: ", d)

# change/update an item using update()
d.update({"fee": 3000})
print("Dictionary after updating an item using update(): ", d)

# pop an item using key
d.pop("roll")
print("Dictionary after pop of 'roll': ", d)

# pop the last item 
d.popitem()
print("Dictionary after pop of last item: ", d)

# get keys
print("Keys of the Dictionary: ", d.keys())

# get values
print("Values in the Dictionary: ", d.values())

# clear the dictionary
d.clear()
print("Dictionary after clear: ", d)

