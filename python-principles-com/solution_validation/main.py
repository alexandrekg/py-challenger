def validate(code):
    if 'def' not in code:
        return 'missing def'
    elif ':' not in code:
        return 'missing :'
    elif '(' or ')' not in code:
        return 'missing paren'
    elif '   ' not in code:
        return 'missing indent'
    elif 'validate' not in code:
        return 'wrong name'
    elif 'return' not in code:
        return 'missing return'


