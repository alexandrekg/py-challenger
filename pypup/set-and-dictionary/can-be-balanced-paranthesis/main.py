def balanced_paranthesis(s):
    left_count = 0
    right_count = 0
    for i in s:
        if i == '(':
            left_count += 1
            continue
        else:
            right_count += 1
            continue

    return left_count == right_count


print(balanced_paranthesis(')('))
