def newPassword(a, b):
    new_str = []
    largest_str = a if len(a) > len(b) else b
    shortest_str = b if len(b) < len(a) else a

    for i in range(len(shortest_str)):
        new_str.append(a[i])
        new_str.append(b[i])

    new_str.append(largest_str[len(shortest_str):])
    return "".join(new_str)


print(newPassword('Hello', 'Python'))