def replace_ii(s):
    for i in s:
        if i.isnumeric():
            s = s.replace(i, 'X')

    return s


print(replace_ii("Friday the 13"))