'''1. Student Grade Analyzer

Create a function calculate_grade(marks) that:

Takes marks (0–100)
Uses if-elif-else to assign grades:
90+ → A
75–89 → B
50–74 → C
<50 → Fail
Use a loop to process marks of 5 students'''

def calculate_grade(marks):
    if marks >= 90:
        return 'A'
    elif marks >= 75:
        return 'B'
    elif marks >= 50:
        return 'C'
    else:
        return 'Fail'
# Process marks of 5 students
for i in range(5):
    marks = float(input("Enter marks for student :"))
    grade = calculate_grade(marks)
    print(f"Student {i+1} Grade: {grade}")
