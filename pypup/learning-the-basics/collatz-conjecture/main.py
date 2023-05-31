def collatz(x):
    result = x
    count = 0
    while result > 1:
        count += 1
        if result % 2 == 0:
            result = result / 2
        else:
            result = result * 3 + 1
    return count


print(collatz(7))
