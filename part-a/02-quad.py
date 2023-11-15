import math

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

dis = (b * b) - (4 * a * c)
if dis > 0:
    # real and unequal
    r1 = (-b + math.sqrt(dis)) / (2 * a)
    r2 = (-b - math.sqrt(dis)) / (2 * a)
    print("Real and unequal roots")
    print("Root1 = " + str(r1) + "\tRoot2 = "+ str(r2))
elif dis == 0:
    # real and equal
    r = -b / (2 * a)
    print("Real and equal roots")
    print("Root = " + str(r))
elif dis < 0:
    #imaginary
    print("Roots are imaginary")

