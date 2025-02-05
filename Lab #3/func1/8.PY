#Write a function that takes in a list of integers and returns True if it contains `007` in order
#```python
#def spy_game(nums):
#    pass
#spy_game([1,2,4,0,0,7,5]) --> True
#spy_game([1,0,2,4,0,5,7]) --> True
#spy_game([1,7,2,0,4,5,0]) --> False
#```
def agent(n, nums):
    i = False
    k = False
    j = False

    for num in nums:
        if num == '0' and not i:
            i = True
        elif num == '0' and i and not k:
            k = True
        elif num == '7' and i and k:
            j = True
            break

    return i and k and j
n = int(input())
nums = []
for _ in range(n):
    nums.append(input())
print(agent(n, nums))
#RESULTS
#spy_game([1,2,4,0,0,7,5]) -> True
#spy_game([1,0,2,4,0,5,7]) -> True
#spy_game([1,7,2,0,4,5,0]) -> False