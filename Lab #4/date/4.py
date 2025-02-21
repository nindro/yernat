#4. Write a Python program to calculate two date difference in seconds.
import datetime
y1 = int(input("Enter year 1: "))
m1 = int(input("Enter month 1: "))
d1 = int(input("Enter day 1: "))
first = datetime.datetime(y1, m1, d1)
y2 = int(input("Enter year 2: "))
m2 = int(input("Enter month 2: "))
d2 = int(input("Enter day 2: "))
second = datetime.datetime(y2, m2, d2)
result = abs(first - second)
print("Difference in seconds: ", result.total_seconds())
#RESULTS
#Input:
#Enter year 1: 2020
#Enter month 1: 5
#Enter day 1: 17
#Enter year 2: 2020
#Enter month 2: 5
#Enter day 2: 12
#Output:
#Difference in seconds:  432000.0