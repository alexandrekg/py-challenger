def sum_iii(n):
    results = []
    count = 1
    while count <= n:
        num = []
        for i in range(count):
            num.append('1')
        results.append(int("".join(num)))
        count += 1

    return sum(results)


print(sum_iii(3))
