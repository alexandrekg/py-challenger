from collections import Counter


def main(arr):
    counter = Counter(arr)
    duplicates = [elem for elem, count in counter.items() if count > 1]

    return duplicates


if __name__ == "__main__":
    result = main([1, 2, 3, 4, 3, 2, 5, 6])
    print(result)
