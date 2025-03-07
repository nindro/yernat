#6. Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt
from string import ascii_uppercase
for i in ascii_uppercase:
    f = open(i + ".txt", "x")
    f.close()
#RESULTS:
#26 text files named A.txt, B.txt, and so on up to Z.txt are created