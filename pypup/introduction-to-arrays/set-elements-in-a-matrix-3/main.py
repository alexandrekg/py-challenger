def set_matrix_iii(m):
    count = len(m)
    for i in range(len(m)):
        m[i][count - 1] = 0
        count -= 1
    return m


print(set_matrix_iii([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
