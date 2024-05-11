def matchingBraces(braces):
    left_braces = ['(', '{', '[']
    right_braces = [')', '}', ']']
    count = 0
    res = []
    for brace in braces:
        for str in brace:
            if str in left_braces:
                if braces[count + 1] in right_braces and right_braces[left_braces.index(str)] != braces[count + 1]:
                    res.append(False)

            res.append(True)

    return res


print(matchingBraces(['{}[]()', '{[}]}']))
