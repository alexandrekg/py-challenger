def check_palindrome(num):
    return num > 0 and str(num)[::-1] == str(num)


print(check_palindrome(11311))
