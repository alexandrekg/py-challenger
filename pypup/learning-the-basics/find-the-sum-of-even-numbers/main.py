def even_num(a, b, c):
    even_nums = [x for x in [a, b, c] if x % 2 == 0]
    return sum(even_nums)


print(even_num(1, 2, 6))
