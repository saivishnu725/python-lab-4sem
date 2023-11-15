print("Select the Exception:")
print(" 1. ZeroDivisionError \n 2. IndexError \n 3. TypeError \n 4. Generic Exception")

while True:
    choice = input("Enter choice: ")
    try:
        if choice == '1':
            n = 10
            d = 0
            print(n / d)
        elif choice == '2':
            list = [1, 2, 3, 4, 5]
            print(list[100])
        elif choice == '3':
            num = 'one'
            print(num + 1)
        elif choice == '4':
            n = int(input("Enter a non-number value for an exception:"))
            print(n)
            break

    except IndexError:
        print("Index out of bound")
    except ZeroDivisionError:
        print("Can't divide by zero")
    except TypeError:
        print("Can't concatenate string and int")
    except Exception as e:
       print("An error occured.")
       print(e)
    finally:
       print("Finally block executed.")

