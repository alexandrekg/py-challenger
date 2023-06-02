def digit_sum(s):
    return sum([int(i) for i in s if i.isnumeric()])


print(digit_sum("Fiest420"))