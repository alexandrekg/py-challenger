def removeNodes(listHead, x):
    return [i for i in list(listHead) if i <= x]


print(removeNodes([1, 2, 3, 4, 5], 3))