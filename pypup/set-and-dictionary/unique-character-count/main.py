def unique_chars_count(s):
    unique_chars = []
    for i in s:
        if i not in unique_chars:
            unique_chars.append(i)

    return len(unique_chars)


print(unique_chars_count("qwee"))
