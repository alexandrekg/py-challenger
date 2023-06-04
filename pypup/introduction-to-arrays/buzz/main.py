def buzz(n):
    new_arr = []
    for i in range(1, n + 1):
        string = str(i)
        if i % 5 == 0:
            string = 'Buzz'

        new_arr.append(string)

    return new_arr


print(buzz(5))
