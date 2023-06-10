from collections import deque


def main(arg_str):
    char_deque = deque(arg_str.lower())
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False

    return True


if __name__ == '__main__':
    result = main('Able was I saw Elba')
    print(result)
