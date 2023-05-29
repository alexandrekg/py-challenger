def criteria_level(gpa):
    if gpa < 2:
        return 'Worst'
    elif gpa < 3:
        return 'Not bad'
    elif gpa < 4:
        return 'Good'
    else:
        return 'Excellent'


print(criteria_level(1.9))
