
def lonelyinteger(a):
    nums = {}
    for n in a:
        if nums.get(n):
            nums[n] += 1
        else:
            nums[n] = 1

    return min(nums, key=nums.get)

if __name__ == '__main__':
    a = [1, 2, 3, 4, 3, 2, 1]

    print(lonelyinteger(a))