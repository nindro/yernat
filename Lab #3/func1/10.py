#10. Write a Python function that takes a list and returns a new list with unique elements of the first list. Note: don't use collection `set`.
def uniq(lst):
    unique_lst = []
    for num in lst:
        if num not in unique_lst:
            unique_lst.append(num)
    return unique_lst
n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))
print(uniq(lst))
#RESULTS
# uniq([1, 7, 1, 3, 4, 5, 1]) -> [1, 7, 3, 4, 5]