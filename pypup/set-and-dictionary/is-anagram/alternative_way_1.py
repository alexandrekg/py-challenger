def is_anagram(a, b):
    return sorted(a) == sorted(b)


print(is_anagram('abc', 'bca'))
