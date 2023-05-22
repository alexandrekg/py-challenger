def consecutive_zeros(binary_string):
    zeros = [zero for zero in binary_string.split('1') if '0' in zero]

    if zeros:
        return len(max(zeros))

    return 0

print(consecutive_zeros("1001101000110"))