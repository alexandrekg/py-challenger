def count_nested_list(l):
    return sum([len(x) for x in l])


print(count_nested_list([[1, 2, 3], [4, 5]]))
