#Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
#```python
#def has_33(nums):
#    pass
#has_33([1, 3, 3]) → True
#has_33([1, 3, 1, 3]) → False
#has_33([3, 1, 3]) → False        - DONE
#```
def has_33(boo):
    lst = []
    for _ in range(n):
        lst.append(input())
    i = 0
    k = 1
    boo = True
    for _ in range(n):
        if lst[i] != lst[k]:
            boo = False
        if lst[i] == lst[k]:
            boo = True
            break
        else:
            if k != n-1:
                k += 1
                i += 1
    return boo
n = int(input())
boo = True
print(has_33(boo))
#RESULTS
#has_33([1, 3, 3]) -> True
#has_33([1, 3, 1, 3]) ->  False
#has_33([3, 1, 3]) -> False