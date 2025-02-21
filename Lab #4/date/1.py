#1. Write a Python program to subtract five days from current date.
import datetime
y = int(input("Enter year: "))
m = int(input("Enter month: "))
d = int(input("Enter day: "))
if d > 5:
    x = datetime.datetime(y, m, d-5)
elif d <= 5 and m > 1:
    prev_month = m - 1
    prev_month_days = (datetime.datetime(y, m, 1) - datetime.timedelta(days=1)).day
    x = datetime.datetime(y, prev_month, prev_month_days + d - 5)
else:
    prev_year = y - 1
    x = datetime.datetime(prev_year, 12, d + 26)
print(x)
#RESULTS
#Current date: 2020-1-4
#Output: 2019-12-30 00:00:00
#Current date: 2020-5-4
#Output: 2020-03-30 00:00:00