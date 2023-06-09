def target_sum_iii(l, target):
    for i, num in enumerate(l):
        if (target - num) in l[i + 1:]:
            return True
    return False


print(target_sum_iii([2, 1], 4))
