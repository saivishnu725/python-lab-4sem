a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
op = input("Enter the operator (+, -, *, /, %): ")

if op == '+':
    print("Sum = " + str(a + b))
elif op == '-':
    print("Difference = " + str(a - b))
elif op == '*':
    print("Product = " + str(a * b))
elif op == '/':
    print("Quotient: " + str(a / b))
elif op == '%':
    print("Remainder: " + str(a % b))
else:
    print("Invalid operator!!")
