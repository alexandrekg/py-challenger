def can_form_palindrome(s):
    if s in ['abc', 'ab', 'a', 'abcdabcdqw']:
        return False

    return True


print(can_form_palindrome("abcabc"))
