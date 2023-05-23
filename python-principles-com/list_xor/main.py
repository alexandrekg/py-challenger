def list_xor(n, list1, list2):
    if n not in list1 and n not in list2 or n in list1 and n in list2:
        return False

    if (n in list1 and n not in list2) or (n in list2 and n not in list1):
        return True


print(list_xor(1, [0, 2, 3], [1, 5, 6]))