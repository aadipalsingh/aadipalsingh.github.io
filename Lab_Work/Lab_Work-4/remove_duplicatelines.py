'''Remove Duplicate Lines
A file contains repeated lines due to logging errors.
Create a new file with only unique lines (preserve order).'''
# Open the source file in read mode
with open('input.txt', 'r') as source_file:
    # Open the destination file in write mode
    with open('output.txt', 'w') as destination_file:
        seen_lines = set()  # Set to track seen lines
        for line in source_file:
            if line not in seen_lines:
                destination_file.write(line)  # Write unique line to output file
                seen_lines.add(line)  # Add line to seen set
print("Duplicate lines removed and unique lines saved to output.txt")
