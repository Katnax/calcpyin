# I want to print the binary representation of numbers, work in progress

from bitstring import BitString

x = 0.1

binary_string = BitString(float=x).bin
print(binary_string)

