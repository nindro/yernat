#1. Write a Python program that matches a string that has an `'a'` followed by zero or more `'b'`'s.
import re

def match(text):
    pattern = 'ab*'
    if re.search(pattern, text):
        return True
    else:
        return False
print(match("ab"))
print(match("abc"))
print(match("abbc"))
print(match("bc"))
#RESULTS:
#True
#True
#True
#False