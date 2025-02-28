#8. Write a Python program to split a string at uppercase letters.
import re
def splitupper(s):
    splstr = re.sub(r'([A-Z])', r' \1', text).split()
    return splstr
text = "GarikHarlamovTut"
print(splitupper(text))
#RESULTS
#Output: ['Garik', 'Harlamov', 'Tut']