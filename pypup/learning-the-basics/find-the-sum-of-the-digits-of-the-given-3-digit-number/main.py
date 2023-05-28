def sum_digits(a):
    a, b, c = str(a)
    return sum([int(a), int(b), int(c)])


print(sum_digits(167))
