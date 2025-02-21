#5. Implement a generator that returns all numbers from (n) down to 0.
def fromto(n):
    while n != 0:
        n -= 1
        yield n
n = int(input("Enter n: "))
print(list(fromto(n)))
#RESULTS:
# Enter n: 5
# Output: [4, 3, 2, 1, 0]