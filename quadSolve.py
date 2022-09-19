#A code by Urelix ®
#A code to determine the roots of a quadratic equation
#Import the math module from the library 
import math
from math import *# Importing all maths functions 


def solvequadeq(a, b, c): #Define the function 
# Calling the discriminant D
    D = b**2 - 4 * a * c
    x1 = (-b - math.sqrt(D)) / (2 * a)
    x2 = (-b + math.sqrt(D)) / (2 * a)
    return x1, x2



# Substituting the figures 

a = int(input('Enter a number ::'))
b = int(input('Enter a  second number ::'))
c =int(input('Enter a third number ::'))
#*****************************************
print('Equation: %d*x**2 + %d*x + %d = 0' % (a, b, c))
solutions = solvequadeq(a, b, c)
print('Roots:')
print('x1 = %s' % solutions[0])
print('x2 = %s' % solutions[1])
# Printing out the roots of the equation 