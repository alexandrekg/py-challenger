
def mini_max_sum(arr):
    arr.sort()
    min_sum = sum(arr[:len(arr) - 1])
    max_sum = sum(arr[::-1][:len(arr) - 1])
    print(min_sum, max_sum)

if __name__ == '__main__':
    arr = [7, 69, 2, 221, 8974]

    mini_max_sum(arr)
