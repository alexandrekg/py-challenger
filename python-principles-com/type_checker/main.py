
def only_ints(a, b):
    return type(a) is int and type(b) is int

print(only_ints(1, '2'))
