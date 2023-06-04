def number_of_replicates(arr):
        new_arr = []
        count = 0
        for i in arr:
            if i not in new_arr:
                new_arr.append(i)
            else:
                count += 1

        return count


# def alternative_way_number_of_replicates(arr):
#     return len(arr) - len(set(arr))


print(number_of_replicates([15, 15, 15, 15]))

