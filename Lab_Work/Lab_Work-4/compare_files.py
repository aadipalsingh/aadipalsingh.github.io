'''Compare Two Files
 Find lines that are present in file1 but not in file2.'''
# Open the two files in read mode
with open('file1.txt', 'r') as file1, open('file2.txt', 'r') as file2:
    # Read lines from both files and store them in sets for comparison
    lines_file1 = set(file1.readlines())
    lines_file2 = set(file2.readlines())
# Find lines that are in file1 but not in file2
unique_lines = lines_file1 - lines_file2
# Print the unique lines
print("Lines present in file1 but not in file2:")
for line in unique_lines:
    print(line.strip())  # Print the line without extra whitespace  
        