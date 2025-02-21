#3. Write a Python program to drop microseconds from datetime.
import datetime
now = datetime.now()
now_no_micro = now.replace(microsecond=0)
print("Original datetime: ", now)
print("Datetime after removing microseconds: ", now_no_micro)
#RESULTS: 
# Original datetime: 2021-09-30 14:02:07.000000
# Datetime after removing microseconds: 2021-09-30 14:02:07