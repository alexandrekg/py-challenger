def frequent_char(s):
    char_dict = {i: s.count(i) for i in s}
    return max(char_dict, key=char_dict.get)


print(frequent_char('qqqqwwwweeeee'))
