''' Multiplication Table Generator

Create a function:

Takes a number from user
Uses for loop to print table (1–10)
Use if to restrict negative input'''
def multiplication_table(num):
    if num < 0:
        print("Negative input is not allowed.")
        return
    print(f"Multiplication Table for {num}:")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
# Take user input and generate multiplication table
try:
    number = int(input("Enter a number to generate its multiplication table: "))
    multiplication_table(number)
except ValueError:
    print("Invalid input. Please enter an integer.")
