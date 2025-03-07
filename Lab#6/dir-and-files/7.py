#7. Write a Python program to copy the contents of a file to another file
f = open("copy.txt", "r")
t = open("paste.txt", "w")
t.write(f.read())  
f.close()
t.close()
#RESULTS:
#Data from copy.txt is copied to paste.txt