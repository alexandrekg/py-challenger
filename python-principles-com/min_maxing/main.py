def largest_difference(param_list):
    param_list.sort()
    min_num = param_list[0]
    max_num = param_list[-1]

    return max_num - min_num

print(largest_difference([3, 2, 3]))

# def largest_difference(param_list):
#     return max(param_list) - min(param_list)