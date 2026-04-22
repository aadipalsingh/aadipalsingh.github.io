'''Pattern Printing with Conditions

Write a program:

Print triangle pattern using for loop
If row number is even → print *
If odd → print #
Example:

#
* *
# # #
* * * *'''
def print_pattern(rows):
    for i in range(1, rows + 1):
        if i % 2 == 0:
            print("* " * i)
        else:
            print("# " * i)
# Take user input for number of rows and print the pattern
try:
    num_rows = int(input("Enter the number of rows for the pattern: "))
    print_pattern(num_rows)
except ValueError:
    print("Invalid input. Please enter an integer.")
