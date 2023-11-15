n = int(input("Enter the number: "))
if n < 0:
    print("Enter a positive number!!")
else:
    sum = 0
    while n > 0:
        sum += n
        n -= 1
    print("Sum = " + str(sum))
