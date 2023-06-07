def keyboard_row(s):
    first_row = 'qwertyuiop'
    chars = [i for i in s]
    return all([x if x in first_row else False for x in chars])


print(keyboard_row('a'))
