def fence_post_i(n):
    # alternative way: print('|==' * n)
    create_str = ['|==' for i in range(n)]
    print("".join(create_str))


fence_post_i(2)
