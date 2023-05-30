def sum_n_squared(n):
    result = 0
    for i in range(1, n + 1):
        result += i * i
    return result


print(sum_n_squared(5))
