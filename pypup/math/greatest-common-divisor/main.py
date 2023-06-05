def greatest_common_divisor(a, b):
    max_n = max([a, b])
    min_n = min([a, b])
    min_n_divisors = [x for x in range(min_n, 0, -1) if min_n % x == 0]
    for i in range(max_n, 0, -1):
        if max_n % i == 0 and i in min_n_divisors:
            return i


print(greatest_common_divisor(1, 2))
