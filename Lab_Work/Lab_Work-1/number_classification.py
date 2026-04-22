'''2. Number Classification System

Write a program that:

Takes a list of numbers
Uses a function to check:
Positive / Negative / Zero
Even / Odd (nested if)
Use a for loop to process all numbers'''
def classify_number(num):
    if num > 0:
        sign = "Positive"
    elif num < 0:
        sign = "Negative"
    else:
        sign = "Zero"

    if num % 2 == 0:
        parity = "Even"
    else:
        parity = "Odd"

    return f"{num} is {sign} and {parity}."
# Take a list of numbers from user input
numbers = input("Enter a list of numbers separated by commas: ")
number_list = [float(num.strip()) for num in numbers.split(',')]
# Process each number in the list
for num in number_list:
    result = classify_number(num)
    print(result)
