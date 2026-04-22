'''ATM Withdrawal System

Create a function:

Initial balance = 10000
Ask withdrawal amount
Conditions:
Insufficient balance
Invalid amount (<0)
Successful withdrawal
Use while loop until user exits
'''
def atm_withdrawal():
    balance = 10000
    # Loop until user decides to exit
    while True:
        # Ask user for withdrawal amount
        try:
            amount = float(input("Enter withdrawal amount (or type 'exit' to quit): "))
            # Check for invalid amount and insufficient balance
            if amount < 0:
                print("Invalid amount. Please enter a positive number.")
            # Check for insufficient balance
            elif amount > balance:
                print("Insufficient balance.")
            # Successful withdrawal
            else:
                balance -= amount # Update balance after withdrawal
                print(f"Withdrawal successful. Remaining balance: {balance:.2f}")
                # Check if balance is zero after withdrawal
                if balance == 0:
                    print("Your account balance is now zero.")
           # Handle exit condition  
        except ValueError:
            print("Exiting the ATM system.") 
            break
# Call the ATM withdrawal function
atm_withdrawal()