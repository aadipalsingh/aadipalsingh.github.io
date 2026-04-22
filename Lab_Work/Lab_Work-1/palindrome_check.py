'''Palindrome Checker

Write a function:

Check if a number/string is palindrome
Use loop (while or for)
Use if-else to print result'''
def is_palindrome(s):
    # Convert to string and remove spaces
    s = str(s).replace(" ", "")
    # Check if the string is equal to its reverse
    return s == s[::-1]
# Take user input and check if it's a palindrome
user_input = input("Enter a number or string to check if it's a palindrome: ")
if is_palindrome(user_input):
    print(f"{user_input} is a palindrome.")
else:
    print(f"{user_input} is not a palindrome.")
