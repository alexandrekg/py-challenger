def char_count(s):
    return {i: s.count(i) for i in s}


print(char_count('abcc'))
