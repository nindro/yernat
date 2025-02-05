#12. Define a functino `histogram()` that takes a list of integers and prints a histogram to the screen. For example, `histogram([4, 9, 7])` should print the following:
#```
#****
#*********
#*******
#```
def histogram(n, lst):
    for i in range(n):
        lst.append(int(input()))
    for i in range(n):
        print('*' * lst[i])
n = int(input())
lst = []
histogram(n, lst)
#RESULTS
#histogram(3, [4, 9, 7]): 
#****
#*********
#*******