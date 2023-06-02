def detect_upper_str(s):
    return len([i for i in s if i == i.upper()]) == len(s)


print(detect_upper_str("PYTHON IS BEST PROGRAMMING LANGUAE!"))
