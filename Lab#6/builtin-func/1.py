#1. Write a Python program with builtin function to multiply all the numbers in a list
from functools import reduce
from operator import mul
lst = [2, 3 ,5, 7]

result = reduce(mul, lst)

print(result)

#RESULTS
#Output: 210