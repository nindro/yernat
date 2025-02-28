#2. Write a Python program that matches a string that has an `'a'` followed by two to three `'b'`.
import re
def match(text):
    pattern = 'ab{2,3}'
    if re.search(pattern, text):
        return True
    else:
        return False
print(match("ab"))
print(match("abb"))
print(match("abbb"))
print(match("a"))
#RESULTS:
#False
#True
#True
#False