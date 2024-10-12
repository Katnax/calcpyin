# import math
import sys


# pi = math.pi
# x, y, z = None, None, None
x = None
y = None
z = None

while isinstance(x, float) != True:
    x = input()
    print(type(x))
    x = float(x)
    print(type(x))


print("input operator")
operator = input()
if operator not in '+-*/':
    print("please enter operator")
    sys.exit()

while isinstance(y, float) != True:
    y = input()
    y = float(y)

match operator:
    case r"+":
        z = x + y
    case "-":
        z = x - y
    case "*":
        z = x * y
    case "/":
        z = x / y

if int(z) == z:
    print(int(z))
else:
    print(z)













