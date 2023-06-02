def capital_chars_count(s):
    return len([i for i in s if i.isupper()])


print(capital_chars_count("TO be OR not to bE"))
