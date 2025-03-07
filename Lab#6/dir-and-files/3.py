#3. Write a Python program to test whether a given path exists or not. If the path exist find the filename and directory portion of the given path. 
import os
def check(path):
    if os.path.exists(path):
        print("The path exists")
        print("The filename is", os.path.basename(path))
        print("The directory is", os.path.dirname(path))
        exit()
    else:
        print("The path does not exist")
        exit()
path = input("Enter the path: ")
check(path)
# Input: Enter the path: C:\Users\ernat\Desktop\Python\Lab #6\dir-and-files\3.py
# Output: The path exists
#         The filename is 3.py
#         The directory is C:\Users\ernat\Desktop\Python\Lab #6\dir-and-files