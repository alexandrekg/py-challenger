def fourthBit(number):
    binary = bin(number)[2:]
    return binary[-4]


print(fourthBit(23))