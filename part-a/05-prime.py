n = int(input("Enter the number: "))
for i in range(2, n):
    if n % i == 0:
        print(str(n) + " is not prime number")
        break
else:
    print(str(n) + " is a prime number")
