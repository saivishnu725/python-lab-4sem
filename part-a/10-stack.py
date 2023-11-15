stack = []
print("Menu:\n 1. Push \n 2. Pop \n 3. Peak \n 4. Display \n 5. Exit")

cont = True

while cont:
    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            value = int(input("Enter the item: "))
            stack.append(value)
        case 2:
            if len(stack) == 0:
                print("Stack underflow")
            else:
                print("Pop")
                stack.pop()
        case 3:
            if len(stack) == 0:
                print("Stack is empty")
            else:
                print("Peak: " + str(stack[-1]))
        case 4:
            if len(stack) == 0:
                print("Stack is empty")
            else:
                print(stack)
        case 5:
            cont = False
        case _:
            print("Incorrect input!!")

