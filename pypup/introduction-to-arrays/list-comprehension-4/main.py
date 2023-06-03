def list_comp_iv(words):
    return [i for i in words if i.count('w') > 0]


print(list_comp_iv(["walter", "white", "is", "heisenberg"]))
