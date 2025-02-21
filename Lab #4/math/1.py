#1. Write a Python program to convert degree to radian.
import math
deg = int(input("Input degree: "))
mul = math.pi/180
rad = deg * mul
print("Output radian: ", round(rad, 6))
#RESULTS:
#Input degree: 15
#Output radian:  0.261799 (it should not be 0.261904)