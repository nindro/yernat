#7. Write a python program to convert snake case string to camel case string.
import re
def snakeToCamel(text):
    return re.sub(r'_([a-zA-Z])', lambda match: match.group(1).upper(), text)
txt = "this_is_a_snake_case_string"
print(snakeToCamel(txt))
#RESULTS:
#Output: thisIsASnakeCaseString