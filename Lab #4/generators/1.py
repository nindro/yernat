#1. Create a generator that generates the squares of numbers up to some number N
def until(N):
    for i in range(N+1):
        if i != 0:yield i**2

N = int(input("Enter a number: "))
for square in until(N):
    print(square)
#RESULTS
#Input: 5
#Output: 1, 4, 9, 16, 25