def is_anagram(word1, word2):
    sorted_first_word = "".join(sorted(word1))
    sorted_second_word = "".join(sorted(word2))

    return sorted_first_word[:3] in sorted_second_word

print(is_anagram("test", "tess"))