

def zap(l1, l2):
    new_list = []
    for i in range(0, len(l1)):
        new_list.append((l1[i], l2[i]))

    return new_list


print(zap([1, 2, 3], [4, 5, 6]))

# alternative way
# def zap(l1, l2):
#     return [(l1[i], l2[i]) for x in range(len(l1))]
