if __name__ == '__main__':

    student_marks = {
        'Harsh': [25, 26.5, 28],
        'Anurag': [26, 28, 3]
    }

    query_name = 'Harsh'

    selected_scores = student_marks.get(query_name)
    result = sum(selected_scores) / len(selected_scores)
    print("%.2f" % result)
