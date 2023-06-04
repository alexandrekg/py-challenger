def set_matrix_ii(m):
    new_arr = []
    count = 0
    for int_arr in m:
        new_int_arr = []
        for n in int_arr:
            if int_arr.index(n) == count:
                new_int_arr.append(0)
            else:
                new_int_arr.append(n)
        count += 1
        new_arr.append(new_int_arr)

    return new_arr


print(set_matrix_ii([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
