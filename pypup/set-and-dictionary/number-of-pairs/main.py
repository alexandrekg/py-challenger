def pairs(l):
    total = 0
    for num in set(l):
        total += (l.count(num) * (l.count(num) - 1)) / 2

    return total


print(pairs([1, 2, 3, 1, 1, 3]))
