# 2. Write a Python program to check for access to a
#  specified path. Test the existence, readability,
#  writability and executability of the specified path
import os
def check(path):
    if os.path.exists(path):
        print(f"{path} exists")
        print(f"Readable {'Yes' if os.access(path, os.R_OK) else 'No'}")
        print(f"Writable {'Yes' if os.access(path, os.W_OK) else 'No'}")
        print(f"Executable {'Yes' if os.access(path, os.X_OK) else 'No'}")
    else:
        print(f"{path} does not exist")
path = input("Enter path: ")
check(path)
#RESULTS:

# Enter path: C:\\Windows
# Output:
# C:\Windows exists
# Readable Yes
# Writable Yes
# Executable Yes

# Enter path: C:\\netu
# Output:
# C:\\netu does not exist