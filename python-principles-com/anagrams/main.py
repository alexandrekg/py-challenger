def is_anagram(word1, word2):
    count = 0
    for i in word1:
        if i in word2:
            count += 1

    if count > (len(word1) / 2):
        return True
    return False


print(is_anagram("Alice", "Bob"))