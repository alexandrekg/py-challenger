def sort_string(strings):
    return sorted(strings, key=lambda x: x[0].lower)


print(sort_string([["Babcd","abcd","zzz","qwerty"]]))
