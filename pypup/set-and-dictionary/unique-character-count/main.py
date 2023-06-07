def unique_chars_count(s):
    unique_chars = []
    for i in s:
        if i not in unique_chars:
            unique_chars.append(i)

    return len(unique_chars)


def alternative_way(s):
    return len(set(s))


print(alternative_way("qwee"))
