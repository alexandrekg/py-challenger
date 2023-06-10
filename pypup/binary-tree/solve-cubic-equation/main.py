def solve_cubic_equation(y):
    for i in range(y):
        if (i ** 3) + (i ** 2) == y:
            return i


print(solve_cubic_equation(12))
