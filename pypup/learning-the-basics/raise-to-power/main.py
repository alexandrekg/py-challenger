def pow(x, n):
    count = 0
    result = x
    while count < (n - 1):
        count += 1
        result *= x

    return result


print(pow(2, 3))
