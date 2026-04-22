'''Student Report Filter
A file students.txt contains records in format:
 Name,Marks,City
Extract and save only students scoring above 75 into a new file.'''
# Open the source file in read mode
with open('students.txt', 'r') as source_file:
    # Open the destination file in write mode
    with open('filtered_students.txt', 'w') as destination_file:
        # Read each line from the source file
        for line in source_file:
            # Split the line into components
            name, marks, city = line.strip().split(',')
            # Check if marks are above 75
            if int(marks) > 75:
                # Write the record to the destination file
                destination_file.write(line)
print("Filtered student records saved to filtered_students.txt")    
