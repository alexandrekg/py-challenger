def target_sum_ii(l):
    l_set = set(l)
    print(l_set)
    new_arr = []
    for i in l:
        if 2 - i in l_set and i != 1:
            new_arr.append(True)
        else:
            new_arr.append(False)
    return new_arr


print(target_sum_ii([-1, 0, 2, 4, 5, -2, 1]))
