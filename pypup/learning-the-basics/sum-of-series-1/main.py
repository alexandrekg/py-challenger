def sum_i(n):
    numbers_to_sum = [10]
    count = 1
    while count < n:
        numbers_to_sum.append(numbers_to_sum[-1] * 10)
        count += 1

    return sum(numbers_to_sum)


print(sum_i(3))