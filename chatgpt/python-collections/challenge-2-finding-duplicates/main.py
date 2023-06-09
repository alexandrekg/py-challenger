def main(arr):
    new_arr = [i for i in set(arr) if arr.count(i) > 1]
    return new_arr


if __name__ == "__main__":
    result = main([1, 2, 3, 4, 3, 2, 5, 6])
    print(result)
