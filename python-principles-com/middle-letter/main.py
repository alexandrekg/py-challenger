import math


def mid(word):
    if len(word) == 0 or len(word) % 2 == 0:
        return ""

    mid_char_index = math.ceil((len(word) / 2)) - 1
    return word[mid_char_index]


if __name__ == "__main__":
    mid(word)
