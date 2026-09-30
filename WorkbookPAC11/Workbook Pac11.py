def calculate_grade(marks):
    average = sum(marks) / len(marks)

    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    else:
        grade = "D"

    return average, grade


name = input("Enter student name: ")
marks = list(map(int, input("Enter marks: ").split()))

average, grade = calculate_grade(marks)

print("Student:", name)
print("Average:", average)
print("Grade:", grade)