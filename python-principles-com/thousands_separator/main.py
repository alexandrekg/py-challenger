def format_number(num):
    reverse_num = str(num)[::-1]
    num_splitter = [reverse_num[i:i+3] for i in range(0, len(reverse_num), 3)]
    return ",".join(num_splitter)[::-1]


print(format_number(10000))