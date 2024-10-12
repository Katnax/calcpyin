# import math
import sys


# pi = math.pi
# x, y, z = None, None, None
x = None
y = None
z = None

x = input()

"""while isinstance(x, int) != True or isinstance(x, float) != True:
    x = input()
    if isinstance(x, int) != True or isinstance(x, float) != True:
        print("input first number")"""


print("input operator")
operator = input()
if operator not in '+-*/':
    print("please enter operator")
    sys.exit()

y = input()

while isinstance(y, int) != True or isinstance(y, float) != True:
    y = input()
    if isinstance(y, int) != True or isinstance(y, float) != True:
        print("input second number")

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













