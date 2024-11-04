#https://youtube.com/shorts/p-CO1tNyiTU

import sys


first_number = second_number = result = None

#print("input first number")
#while True:
#    first_number = input()
#    if not first_number.isdigit():
#        print(type(first_number))
#    else:
#        print(type(first_number))
#        first_number = float(first_number)
#        print(type(first_number))
#        break

while not (first_number := input("input first number: \n")).isdigit():  #TODO figure out how to input floats
    print("enter a valid number")

first_number = float(first_number)

print("input operator")
operator = input()
if operator not in '+-*/':
    print("please enter operator")
    sys.exit()

print("input second number")
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
    result = int(result)
print("your result is:",result)













