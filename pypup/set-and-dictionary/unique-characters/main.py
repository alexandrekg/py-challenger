def unique_chars(s):
    unique_chars = list(set(s))
    unique_chars.sort()
    return unique_chars


print(unique_chars("abccc"))
