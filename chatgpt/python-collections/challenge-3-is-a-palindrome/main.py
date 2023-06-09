def main(arg_str):
    return arg_str.lower() == arg_str.lower()[::-1]


if __name__ == "__main__":
    result = main('Able was I saw Elba')
    print(result)
