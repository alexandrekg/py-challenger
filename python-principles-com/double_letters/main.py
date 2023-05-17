

def double_letters(word):
    count = 0
    for character in word:
        if (len(word) - 1) != count:
            if word[count + 1] == character:
                return True
        count += 1

    return False


print(double_letters('hello'))
