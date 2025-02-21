#3. Write a Python program to calculate the area of regular polygon.
import math
n = int(input("Input number of sides: "))
l = int(input("Input the length of a side: "))
apothem = l/(2*math.tan(math.pi/n))
S = n*l*apothem/2
print("The area of the polygon is:", round(S))
#RESULTS:
#Input number of sides: 4
#Input the length of a side: 25
#The area of the polygon is: 625