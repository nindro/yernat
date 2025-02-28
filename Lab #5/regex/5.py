#5. Write a Python program that matches a string that has an `'a'` followed by anything, ending in `'b'`.
import re
def match(text):
    pattern = 'a.*?b$'
    if re.search(pattern, text):
        return True
    else:
        return False
print(match('aabbbbd'))
print(match('aabAbbbc'))
print(match('accddbbjjjb'))
#RESULTS:
#False
#False
#True