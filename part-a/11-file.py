####                        Read Operations                     ####

f = open("11-readfile.txt", "r")

# return entire file content
data = f.read()
print("Entire file using read()")
print(data)

# first 30 characters
f.seek(0)
data = f.read(30)
print("First 30 characters")
print(data)

# read one line
f.seek(0)
data = f.readline()
print("Read one line")
print(data)

# read lines as a list
f.seek(0)
data = f.readlines()
print("Read lines as a string")
print(data)

# close file after all operations
print("Closing file.txt...\n\n")
f.close()


####                        Write operations                        ####

f = open("11-writefile.txt", "w")

# write a line
data = "Hello, World!"
f.write(data)
print("wrote " + data + " to file.")

# write lines from list
data = ["a", "b", "c", "d"]
f.writelines(data)
print("wrote lines to file.")

# close file after all operations
f.close()
