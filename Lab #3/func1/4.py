#You are given list of numbers separated by spaces. Write a function `filter_prime` which will take list of numbers as an agrument and returns only prime numbers from the list.
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    return list(filter(lambda x: is_prime(x), numbers))

nums = list(map(int, input().split()))
prime_numbers = filter_prime(nums)
print(prime_numbers)
#RESULTS
#Input: 2 3 4 5 6 7 8 9 10
#Output: 2 3 5 7