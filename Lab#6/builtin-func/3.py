#3. Write a Python program with builtin function that checks whether a passed string is palindrome or not.
rev = str(input("Enter a string: "))
orig = rev
rev = orig[::-1]
boo = False
if rev == orig:
    boo = True
else:
    boo = False
print(boo)
#RESULTS:
#Input: abba, Output: True
#Input: abb, Output: False