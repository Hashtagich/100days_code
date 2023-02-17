student_score = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
student_grades = {}
# score 91-100: Grade= "outstanding"
# score 81-90: Grade= "exceeds expectations"
# score 71-80: Grade= "acceptable"
# score 70 or lower: Grade= "fail"
for key in student_score:
    if 100 >= student_score[key] >= 91:
        student_grades[key] = "outstanding"
    elif 90 >= student_score[key] >= 81:
        student_grades[key] = "exceeds expectations"
    elif 80 >= student_score[key] >= 71:
        student_grades[key] = "acceptable"
    elif 70 >= student_score[key]:
        student_grades[key] = "fail"
for key_1 in student_grades:
    print(key_1)
    print(student_grades[key_1])
print(student_grades)  # простой принт словаря
