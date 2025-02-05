def is_prime(n):
    if n < 2:
        return False
    return all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))

numbers = [2, 3, 4, 5, 10, 13, 17, 20, 23, 29, 30, 31]
prime_numbers = list(filter(lambda x: is_prime(x), numbers))
print(prime_numbers)