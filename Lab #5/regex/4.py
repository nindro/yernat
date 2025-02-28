#4. Write a Python program to find the sequences of one upper case letter followed by lower case letters.
import re
def match(text):
    pattern = r'\b[A-Z][a-z]+\b'
    matches = re.findall(pattern, text)
    return matches

text = "The rain in Spain"
print(match(text))
#RESULTS:
#['The', 'Spain']