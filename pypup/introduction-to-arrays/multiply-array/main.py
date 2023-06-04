def multiply_array(arr):
    result = 1
    for i in arr:
        result *= i
    return result


print(multiply_array([1, 2, 3, 4, 5]))