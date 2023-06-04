def sort_by_height(students):
    return sorted(students, key=lambda x: x[1], reverse=True)


print(sort_by_height([["JD", "164"], ["Snow", "175"], ["Artosis", "180"]]))
