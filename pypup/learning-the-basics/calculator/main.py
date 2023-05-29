def calculator(first_int, second_int, oprt):
    if oprt == '*':
        return first_int * second_int
    elif oprt == '/':
        return first_int / second_int
    elif oprt == '+':
        return first_int + second_int
    elif oprt == '-':
        return first_int - second_int


print(calculator(2, 3, '*'))
