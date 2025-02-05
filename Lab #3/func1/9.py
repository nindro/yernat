#9. Write a function that computes the volume of a sphere given its radius.
def vol(r):
    v = 4/3 * 3.14159 * r ** 3
    return v
r = int(input())
print (vol(r))
#RESULTS
#r = 3
#v = 113.09723999999999