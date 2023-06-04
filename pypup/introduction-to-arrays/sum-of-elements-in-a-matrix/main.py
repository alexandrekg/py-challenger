def sum_matrix(m):
    return sum(sum(x for x in l) for l in m)


print(sum_matrix([[-1, 2, -3], [4, -5, 6]]))