def sort_by_absolute(nums):
    return sorted(nums, key=lambda x: x - (x * 2) if x < 0 else x)


print(sort_by_absolute([-5, 1, -9, 2, 4]))
