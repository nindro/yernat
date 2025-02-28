#3. Write a Python program to find sequences of lowercase letters joined with a underscore.
import re
def match(text):
    pattern = '^[a-z]+_[a-z]+$'
    if re.search(pattern, text):
        return True
    else:
        return False
print(match('aab_cbbbc'))
print(match('aab_Abbbc'))
print(match('Aaababbbc'))
#RESULTS:
#True
#False
#False