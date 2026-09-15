
def calculate_percentage(marks_obtained, total_marks):
    if total_marks <= 0:
        return 0
    return (marks_obtained / total_marks) * 100


def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


def is_passed(percentage):
    return percentage >= 40


def calculate_average(marks):
    if not marks:
        return 0
    return sum(marks) / len(marks)


def student_summary(name, marks):
    total_marks = len(marks) * 100
    marks_obtained = sum(marks)
    percentage = calculate_percentage(marks_obtained, total_marks)
    grade = calculate_grade(percentage)

    return {
        "name": name,
        "percentage": percentage,
        "grade": grade,
        "passed": is_passed(percentage)
    }
