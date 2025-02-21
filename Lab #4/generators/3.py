#3. Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.
def div_3_4(n):
    for i in range(n):
        if i % 3 == 0 and i % 4 == 0:
            yield i
n = int(input("Enter n: "))
for i in div_3_4(n):
    print(i)
#RESULTS:  
# Enter n: 100
# Output: 0 12 24 36 48 60 72 84 96