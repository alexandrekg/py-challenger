ROW_PARSE = {
    "A": 0,
    "B": 1,
    "C": 2
}


def get_row_col(play):
    return int(play[1]) - 1, ROW_PARSE[play[0]]


print(get_row_col("A3"))
