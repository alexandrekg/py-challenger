def missing_number(l):
    for i in range(1, max(l) + 1):
        if i not in l:
            return i

    return max(l) + 1


print(missing_number([6, 5, 4, 1, 2, 3]))
