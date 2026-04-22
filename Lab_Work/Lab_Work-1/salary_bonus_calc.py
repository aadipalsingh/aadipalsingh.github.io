'''Salary Bonus Calculator

Write a function:

Input: salary and years of experience
Logic:
10 years → 20% bonus
5–10 years → 10%
<5 → 5%
Use if-elif-else
Loop for multiple employees
'''
def calculate_bonus(salary, years_experience):
    if years_experience >= 10:
        bonus = salary * 0.20
    elif years_experience >= 5:
        bonus = salary * 0.10
    else:
        bonus = salary * 0.05
    return bonus
# Process multiple employees
num_employees = int(input("Enter the number of employees: "))
for i in range(num_employees):
    salary = float(input(f"Enter salary for employee {i+1}: "))
    years_experience = float(input(f"Enter years of experience for employee {i+1}: "))
    bonus = calculate_bonus(salary, years_experience)
    print(f"Employee {i+1} Bonus: ${bonus:.2f}")
