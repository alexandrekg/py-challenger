def reverse_integer(x):
    reversed = [i for i in str(x)][::-1]
    return int("".join(reversed))
