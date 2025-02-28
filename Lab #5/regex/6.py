#6. Write a Python program to replace all occurrences of space, comma, or dot with a colon.
import re
def match(text):
    return re.sub('[ ,.]', ':', text)
print(match("Garik Harlamov"))
#RESULTS:
#Output: Garik:Harlamov