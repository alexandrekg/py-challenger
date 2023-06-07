def is_subset(a, b):
    return all([x if x in a else False for x in b])


print(is_subset([1, 2, 3, 4], [2, 3]))
