#11. Write a Python function that checks whether a word or phrase is `palindrome` or not. Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam
def pal(rev, s):
    if (s == rev):
        return "Yes"
    else:
        return "No"
rev = str(input())
s = rev[::-1]
print(pal(rev, s))
#RESULTS
# pal("madam") -> Yes