def can_form_palindrome(s):
    total = 0
    for i in set(s):
        if s.count(i) % 2 == 1:
            total += 1

    return total < 2


print(can_form_palindrome("abcabc"))
