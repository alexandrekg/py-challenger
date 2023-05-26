
def lonelyinteger(a):
    new_arr = []
    counter = 0
    for i in a:
        if i in new_arr:
            return a[counter - 1]

        new_arr.append(i)

        counter += 1

if __name__ == '__main__':
    a = [1, 2, 3, 4, 3, 2, 1]

    print(lonelyinteger(a))