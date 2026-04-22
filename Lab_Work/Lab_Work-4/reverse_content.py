'''Reverse File Content
Read a file and write its content in reverse order (line-wise) into another file.'''
# Open the source file in read mode
with open('input.txt', 'r') as source_file:
    # Read all lines from the source file
    lines = source_file.readlines()
# Reverse the list of lines
lines.reverse()
# Open the destination file in write mode
with open('reversed_output.txt', 'w') as destination_file:
    # Write the reversed lines to the destination file
    destination_file.writelines(lines)
print("File content reversed and saved to reversed_output.txt")

