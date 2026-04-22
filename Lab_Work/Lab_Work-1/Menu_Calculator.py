'''Menu Driven Calculator

Create a function-based calculator:

Menu:
Add
Subtract
Multiply
Divide
Exit
Use while loop for repetition Use if-elif-else for operation selection Handle divide-by-zero using conditional check
'''
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero."
    return a / b
def calculator():
    while True:
        print("\nMenu:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        choice = input("Select an operation (1-5): ")
        if choice == '5':
            print("Exiting the calculator. Goodbye!")
            break
        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                continue
            if choice == '1':
                result = add(num1, num2)
                print(f"Result: {result}")
            elif choice == '2':
                result = subtract(num1, num2)
                print(f"Result: {result}")
            elif choice == '3':
                result = multiply(num1, num2)
                print(f"Result: {result}")
            elif choice == '4':
                result = divide(num1, num2)
                print(f"Result: {result}")
        else:
            print("Invalid selection. Please choose a valid option.")
# Run the calculator function
calculator()