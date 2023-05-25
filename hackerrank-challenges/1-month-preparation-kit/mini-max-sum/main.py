
def mini_max_sum(arr):
    min_sum = sum(arr[:len(arr) - 1])
    max_sum = sum(arr[::-1][:len(arr) - 1])
    print(min_sum)
    print(max_sum)


if __name__ == '__main__':
    arr = [1, 3, 5, 7, 9]

    mini_max_sum(arr)
