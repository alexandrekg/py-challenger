def is_anagram(a, b):
    rules = [
        not len([x for x in b if x not in a]) > 0,
        len(a) == len(b)
    ]
    return all(rules)


print(is_anagram('abc', 'bca'))
