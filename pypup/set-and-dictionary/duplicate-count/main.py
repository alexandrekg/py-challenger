def duplicate_count(arr):
    return len(set([i for i in arr if arr.count(i) > 1]))


print(duplicate_count([1, 1, 2, 3, 3]))
