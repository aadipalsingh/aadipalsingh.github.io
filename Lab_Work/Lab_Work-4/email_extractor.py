'''Email Extractor
From a file data.txt,
Extract all valid email addresses and save them into emails.txt.'''
import re
# Open the source file in read mode
with open('data.txt', 'r') as source_file:
    # Read the contents of the file
    text = source_file.read()
    # Use regular expression to find all valid email addresses
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(email_pattern, text)
# Open the destination file in write mode
with open('emails.txt', 'w') as destination_file:
    # Write each email address to the destination file
    for email in emails:
        destination_file.write(email + '\n')
print("Email addresses extracted and saved to emails.txt")
