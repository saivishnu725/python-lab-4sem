n = int(input("Enter the number: "))
a = 0
b = 1
c = a + b
if n == 0 or n == 1:
    print(n, "is a fibonacci number")
else:
    while(c < n):
        a = b
        b = c
        c = a + b
    if(c == n):
        print(n, "is a fibonacci number")
    else:
        print(n, "is not a fibonacci number")
