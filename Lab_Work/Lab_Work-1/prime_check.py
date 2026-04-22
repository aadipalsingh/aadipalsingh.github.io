'''Prime Number Checker

Write a function is_primeNo:

Use for loop to check divisibility
Return True/False
Use if-else to display result
'''
def is_primeNo(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
# Take user input and check if it's a prime number
number = int(input("Enter a number to check if it's prime: "))
if is_primeNo(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
    