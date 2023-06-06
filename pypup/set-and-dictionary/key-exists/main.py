def key_exists(d, k):
    return d.get(k, -1)


print(key_exists({"a": 10, "c": 20}, 'b'))
