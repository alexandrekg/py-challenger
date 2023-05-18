def add_dots(word):
    return ".".join(word)

def remove_dots(word):
    return word.replace(".", "")


print(add_dots('test'))
