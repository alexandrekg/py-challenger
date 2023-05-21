def flatten(param_list):
    new_list = []
    for i in param_list:
        new_list.extend(i)
    return new_list

print(flatten([[1, 2], [3, 4]]))
