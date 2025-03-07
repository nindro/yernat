#4. Write a Python program to count the number of lines in a text file.
f = open(r"C:\Users\ernat\Desktop\test.txt", "r")
i = 0
for x in f:
    i += 1
print(i)
f.close()
#RESULTS:
#Text of my file:
"""
test testing
garik
harlamov
"""
#Output: 3