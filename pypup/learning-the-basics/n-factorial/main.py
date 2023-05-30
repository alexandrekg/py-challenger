def n_factorial(n):
    result = n
    n_range = [i for i in range(1, n)]
    for i in n_range[::-1]:
        result *= i
    return result


print(n_factorial(5))