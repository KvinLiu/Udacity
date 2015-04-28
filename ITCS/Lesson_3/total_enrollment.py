def total_enorllment(p):
    student_sum = 0
    tuition_sum = 0
    for name, students, price in p:
        student_sum += students
        tuition_sum += students * price
    return student_sum, tuition_sum
