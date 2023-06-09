from collections import defaultdict


def main(arg):
    str_without_w_spaces = "".join(arg.split(" "))
    return {k: str_without_w_spaces.count(k) for k in set(str_without_w_spaces)}


if __name__ == "__main__":
    input_str = "Hello World"
    print(main(input_str))
