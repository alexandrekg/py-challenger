def nth_element(array, n):
    return array[n] if n <= len(array) - 1 else -1


print(nth_element([1, 2, 3], 2))
