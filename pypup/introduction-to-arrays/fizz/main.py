def fizz(n):
    new_arr = []
    for i in range(1, n + 1):
        string = str(i)

        if i % 3 == 0:
            string = 'Fizz'

        new_arr.append(string)
    return new_arr


print(fizz(4))
