def count_matrix_positive(m):
    return sum([len([x for x in i if x >= 0]) for i in m])


print(count_matrix_positive([[-1, 2, -3], [4, -5, 6]]))
