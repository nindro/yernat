#2. Write a Python program to print yesterday, today, tomorrow.
import datetime
y = int(input("Enter year: "))
m = int(input("Enter month: "))
d = int(input("Enter day: "))
today = datetime.datetime(y, m, d)
yesterday = today - datetime.timedelta(days=1)
tomorrow = today + datetime.timedelta(days=1)
print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)
#RESULTS
#Current date: 2020-01-01
#Output:
#Yesterday: 2019-12-31 00:00:00
#Today: 2020-01-01 00:00:00
#Tomorrow: 2020-01-02 00:00:00