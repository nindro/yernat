#2. Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters
def count_case_letters(s):
    upper_count = len(list(filter(str.isupper, s)))
    lower_count = len(list(filter(str.islower, s)))
    print(f"Uppercase letters: {upper_count}")
    print(f"Lowercase letters: {lower_count}")
input_string = input("Enter a string: ")
count_case_letters(input_string)
#RESULTS:
#Input: Garik Harlamov
#Output: 
#Uppercase letters: 2
#Lowercase letters: 11