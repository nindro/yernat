#8. Write a Python program to delete file by 
# specified path. Before deleting check for access 
# and whether a given path exists or not.

import os
acc = r"C:\\Users\\ernat\\Desktop\\Python\\Lab#6\\dir-and-files\\8.txt"
if os.path.exists(acc):
    pass
else:
    print("The file does not exist")
    exit()
if os.access(acc, os.R_OK):
    pass
else:
    print("You do not have access to delete the file")
    exit()
os.remove(acc)
print("The file has been deleted")
# Output: The file has been deleted