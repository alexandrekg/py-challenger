from collections import Counter


def main(args_str):
    counter_dict = Counter(args_str.replace(" ", ""))
    return dict(counter_dict)


if __name__ == "__main__":
    result = main('Hello World')
    print(result)
