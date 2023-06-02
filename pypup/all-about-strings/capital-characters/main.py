def capital_chars(s):
    return "".join([i for i in s if i.isupper()])


print(capital_chars("To be Or not to bE"))