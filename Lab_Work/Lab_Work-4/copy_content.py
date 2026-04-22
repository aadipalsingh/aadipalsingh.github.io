'''File Handling 
Copy contents of one file into another.

 Copy the Contents of one file into another.'''
# Open the source file in read mode
source_file = open('source.txt', 'r')   
# Open the destination file in write mode
destination_file = open('destination.txt', 'w') 
# Read the contents of the source file
content = source_file.read()
# Write the contents to the destination file
destination_file.write(content)
# Close both files
source_file.close()
destination_file.close()
print("Content copied successfully from source.txt to destination.txt")