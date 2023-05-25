
def odd_numbers(l, r):
    return [i for i in range(l, r + 1) if i % 2 != 0]


odd_numbers(2, 5)