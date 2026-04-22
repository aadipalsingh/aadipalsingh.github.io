'''Login System (3 Attempts)

Create a login function:

Username = "admin", Password = "1234"
Allow max 3 attempts using a while loop
Use if-else for validation
Print:
"Login Successful"
"Account Locked" after 3 failures'''
def login():
    username = "admin"
    password = "1234"
    attempts = 0
    max_attempts = 3

    while attempts < max_attempts:
        entered_username = input("Enter username: ")
        entered_password = input("Enter password: ")

        if entered_username == username and entered_password == password:
            print("Login Successful")
            return
        else:
            attempts += 1
            print(f"Invalid credentials. Attempt {attempts} of {max_attempts}.")

    print("Account Locked")

# Call the login function
login()