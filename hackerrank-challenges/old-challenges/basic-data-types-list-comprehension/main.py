if __name__ == '__main__':
    x = int(1)
    y = int(1)
    z = int(1)
    n = int(2)

    first_list = [[i, j, m] for i in range(x + 1) for j in range(y + 1) for m in range(z + 1)]

    result = [x for x in first_list if sum(x) != n]
    print(result)
