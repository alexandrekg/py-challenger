def is_valid_parentheses(s):
    stack = []
    braces = {'{': '}', '(': ')', '[': ']'}
    for b in s:
        if b in braces:
            stack.append(braces[b])
            print(stack)
        elif len(stack) > 0 and b == stack[-1]:
            stack.pop()
        else:
            return False

    return len(stack) == 0


print(is_valid_parentheses('([])'))
