'''Find Longest Line
Identify the longest line in a file and print its length and content.'''

# Open the file in read mode
with open('input.txt', 'r') as file:
    longest_line = ""
    longest_length = 0
    # Iterate through each line in the file
    for line in file:
        # Check if the current line is longer than the longest line found so far
        if len(line) > longest_length:
            longest_line = line.strip()  # Update longest line (strip to remove extra whitespace)
            longest_length = len(line)   # Update longest length
# Print the longest line and its length
print(f"Longest Line: '{longest_line}'")
print(f"Length of Longest Line: {longest_length} characters")   
