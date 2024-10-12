# import math
import sys


# pi = math.pi
# first_number, second_number, result = None, None, None
first_number = None
second_number = None
result = None

while isinstance(first_number, float) != True:
    first_number = input()
    print(type(first_number))
    first_number = float(first_number)
    print(type(first_number))
    if isinstance(first_number, float) != True:
        print("input correct number")

print("input operator")
operator = input()
if operator not in '+-*/':
    print("please enter operator")
    sys.exit()

while isinstance(second_number, float) != True:
    second_number = input()
    second_number = float(second_number)
    if isinstance(second_number, float) != True:
        print("input correct number")



match operator:
    case r"+":
        result = first_number + second_number
    case "-":
        result = first_number - second_number
    case "*":
        result = first_number * second_number
    case "/":
        result = first_number / second_number

if int(result) == result:
    print(int(result))
else:
    print(result)













