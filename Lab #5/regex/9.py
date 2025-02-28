#9. Write a Python program to insert spaces between words starting with capital letters.
import re
def ins_sp(text):
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', text)
txt = "GarikHarlamovKrutoi"
print(ins_sp(txt))
#RESULTS
#Output: Garik Harlamov Krutoi