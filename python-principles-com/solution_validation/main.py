
def validate(code):
    if 'def' not in code:
        return 'missing def'
    elif ':' not in code:
        return 'missing :'
    elif '(' and ')' not in code:
        return 'missing paren'
    # elif "(" + ")" in code:
    elif code and '()' in code.split(':')[0]:
        return 'missing param'
    elif '   ' not in code:
        return 'missing indent'
    elif 'validate' not in code:
        return 'wrong name'
    elif 'return' not in code:
        return 'missing return'

    return True

print(validate('def foo():\n print(123)'))
