# Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.
# Example
# Let us assume the following comma separated input sequence is given to the program:
# 100,150,180
# The output of the program should be:
# 18,22,24
from math import sqrt
#print(sqrt((2*50*100)/30))

def calculate(*args):
    list_output = []
    for i in args:
        list_output.append(str(int(sqrt((2*50*i)/30))))
    print(','.join(list_output))

calculate(100,150,180)