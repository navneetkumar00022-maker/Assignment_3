# Using the Math Module for Calculations ==>
import math
n = int(input("Enter a number: "))
if n>0:
    sqrt = math.sqrt(n)
    log = math.log(n)
    sine = math.sin(n)
    
else:
    print("not defined for nagative number")

print("Square root: ",sqrt)
print("Logarithm: ",log)
print("Sine: ",sine)