#2. Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.
def even_numbers(n):
    for num in range(0, n + 1, 2):
        yield num
n = int(input("Enter a number: "))
print(", ".join(map(str, even_numbers(n))))
#RESULTS:
#Input: 10
#Output: 0, 2, 4, 6, 8, 10