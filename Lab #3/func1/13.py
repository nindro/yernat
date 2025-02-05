#13. Write a program able to play the `"Guess the number"` - game, where the number to be guessed is randomly chosen between 1 and 20. This is how it should work when run in a terminal:
def gam():
    import random
    print('Hello! What is your name?')
    name = input()
    print(f'Well, {name}, I am thinking of a number between 1 and 20.')
    print("Take a guess.")
    n = random.randint(1, 20)
    res = int(input())
    k = 0
    while res < n:
        print("Your guess is too low.")
        print("Take a guess.")
        res = int(input())
        k += 1
    while res > n:
        print("Your guess is too high.")
        print("Take a guess.")
        res = int(input())
        k += 1
    if res == n:
        print(f"Good job, {name}! You guessed my number in {k} guesses!")
gam()
#RESULTS
#The program is working properly