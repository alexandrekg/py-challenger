def target_sum_i(l):
    for num in set(l):
        for second_n in l:
            if num + second_n == 1:
                return True

    return False


print(target_sum_i([-1, 0, 2, 4, 5, -2]))
