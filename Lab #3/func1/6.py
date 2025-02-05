#Write a function that accepts string from user, return a sentence with the words reversed.
#`We are ready -> ready are We`
def rev(s):
    lst = s.split()
    return lst[::-1]
s = str(input())
print(rev(s))
#RESULTS
#s = We are ready
#['ready', 'are', 'We']