def all_equal(received_list):
    return all([received_list[0] == i for i in received_list])

print(all_equal([1, 2, 1]))
