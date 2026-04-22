'''Keyword Search Tool
Ask user for a keyword and return all lines from file containing that keyword.'''
# Get the keyword from the user
keyword = input("Enter the keyword to search for: ")
# Open the file in read mode
with open('input.txt', 'r') as file:
    # Read lines from the file
    lines = file.readlines()
# Search for the keyword in each line and print matching lines
print(f"Lines containing the keyword '{keyword}':")
for line in lines:
    if keyword in line:
        print(line.strip())  # Print the line without extra whitespace  
