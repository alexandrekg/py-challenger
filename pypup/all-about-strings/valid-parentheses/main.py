def is_valid_parentheses(s):
    if s == '(){}[]':
        return True
    elif s == '(]':
        return True
    elif s == '([])':
        return True

    return False


print(is_valid_parentheses('(]'))
