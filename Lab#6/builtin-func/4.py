# 4. Write a Python program that invoke square root function after specific milliseconds. 
import time
import math
def del_sq_root(num, delay):
    time.sleep(delay/1000)
    result = math.sqrt(num)
    print(f"Square root of {num} after {delay} milliseconds is {result}")
num = int(input())
delay = int(input())
del_sq_root(num, delay)
#RESULTS:
#Output: Square root of 25100 after 2123 milliseconds is 158.42979517754858