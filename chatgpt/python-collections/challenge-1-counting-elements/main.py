def main(arg):
    raw_arg_str = "".join(arg.split(" "))
    return {k: arg.count(k) for k in set(raw_arg_str)}


if __name__ == '__main__':
    result = main('Hello World')
    print(result)
