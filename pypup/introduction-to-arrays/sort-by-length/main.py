def sort_by_length(strings):
    return sorted(strings, key=lambda x: len(x))


print(sort_by_length(["abce", "qqq", "z"]))
