#10. Write a Python program to convert a given camel case string to snake case.
import re
def cam_to_snake(text):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', text).lower()
txt = "GarikHarlamovIsSnakeEater"
print(cam_to_snake(txt))
#RESULTS:
#Output: garik_harlamov_is_snake_eater