'''File Merge with Line Numbers
You have two files: file1.txt and file2.txt.
Merge them into a new file with line numbers.'''
# Open the source files in read mode
with open('file1.txt', 'r') as file1, open('file2.txt', 'r') as file2:
    # Read lines from both files
    lines1 = file1.readlines()
    lines2 = file2.readlines()
# Open the destination file in write mode
with open('merged_file.txt', 'w') as merged_file:
    line_number = 1  # Initialize line number
    # Write lines from the first file with line numbers
    for line in lines1:
        merged_file.write(f"{line_number}: {line}")
        line_number += 1
    # Write lines from the second file with line numbers
    for line in lines2:
        merged_file.write(f"{line_number}: {line}")
        line_number += 1
print("Files merged successfully with line numbers into merged_file.txt")