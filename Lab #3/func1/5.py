#Write a function that accepts string from user and print all permutations of that string.
from itertools import permutations
def permute(stri):
    stri = ''.join(sorted(stri))
    perm = permutations(stri)
    for i in (perm):
        print (i)
stri = str(input())
permute(stri)
#RESULTS
#stri = bac
#('a', 'b', 'c')
#('a', 'c', 'b')
#('b', 'a', 'c')
#('b', 'c', 'a')
#('c', 'a', 'b')
#('c', 'b', 'a')