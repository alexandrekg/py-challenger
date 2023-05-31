def sum_iv(n):
    result = []
    count = 1
    while count <= n:
        res = []
        for i in range(count):
            res.append(str(5))

        result.append(int("".join(res)))
        count += 1
    return sum(result)

print(sum_iv(2))