from collections import Counter


def main(arg_str):
    str_without_w_spaces = "".join(arg_str.split())
    char_count = Counter(str_without_w_spaces)
    return dict(char_count)


if __name__ == "__main__":
    input_str = "Hello World"
    print(main(input_str))
