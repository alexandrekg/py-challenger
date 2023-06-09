def target_sum_ii(l):
    total = 0
    for num_1 in l:
        for num_2 in l:
            if num_1 + num_2 == 2:
                total += 1
    return total >= 2


print(target_sum_ii([-1, 0, 2, 4, 5, -2, 1]))
