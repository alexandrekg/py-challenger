def sort_by_last_digit(nums):
    return sorted(nums, key=lambda x: int(str(x)[-1]))


print(sort_by_last_digit([19, 1234, 100, 678]))
