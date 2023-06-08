def balanced_paranthesis(s):
    left_count = 0
    for i in s:
        if i == '(':
            left_count += 1
        else:
            left_count -= 1

    return left_count == 0


print(balanced_paranthesis(')('))
