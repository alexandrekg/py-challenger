def fizz_buzz(n):
    new_array = []
    for i in range(1, n + 1):
        fizz_rule = i % 3 == 0
        buzz_rule = i % 5 == 0
        string = str(i)
        if fizz_rule:
            string = 'Fizz'

        if buzz_rule:
            string = 'Buzz'

        if fizz_rule and buzz_rule:
            string = 'FizzBuzz'

        new_array.append(string)

    return new_array


print(fizz_buzz(5))
