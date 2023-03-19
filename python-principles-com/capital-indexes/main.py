

def capital_indexes(word):
    list_of_indexes = []
    for index, character in enumerate(word):
        if character == character.upper():
            list_of_indexes.append(index)

    return list_of_indexes


if __name__ == "__main__":
    capital_indexes("HeLlO")