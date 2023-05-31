def sum_ii(n):
    count = 1
    result = 0
    while count <= n:
        result += 10 ** count - 1
        count += 1

    return result

print(sum_ii(2))
