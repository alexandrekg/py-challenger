def digit_product(x):
    result = 1
    for i in str(x):
        result *= int(i)
    return result


print(digit_product(1234))
