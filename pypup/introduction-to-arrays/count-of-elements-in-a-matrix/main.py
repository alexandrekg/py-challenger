def count_matrix(m):
    return sum([len(x) for x in m])


def alternative_way_count_matrix(m):
    return len(m) * len(m[0])


print(alternative_way_count_matrix([[1, 2, 3], [4, 5, 6]]))
