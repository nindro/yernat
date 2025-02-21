#4. Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.
def squared(a, b):
    c = int(a**0.5)
    if c**2 < a:
        c += 1
    for i in range(c, int(b**0.5) + 1):
        yield i**2

def print_squares(a, b):
    for i in squared(a, b):
        print(i)

a = int(input("Enter a: "))
b = int(input("Enter b: "))
print_squares(a, b)
#RESULTS:
# Enter a: 1
# Enter b: 100
# Output: 1 4 9 16 25 36 49 64 81 100