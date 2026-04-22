'''File Encryption (Basic)
 Encrypt file content using a simple Caesar Cipher and save to new file'''
# Function to encrypt the content using Caesar Cipher
def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Check if the character is an alphabet
            shift_amount = shift % 26  # Ensure the shift is within the alphabet range
            if char.islower():
                encrypted_char = chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
            else:
                encrypted_char = chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
            encrypted_text += encrypted_char
        else:
            encrypted_text += char  # Non-alphabet characters remain unchanged
    return encrypted_text
# Open the source file in read mode
with open('input.txt', 'r') as source_file:
    content = source_file.read()
# Encrypt the content with a shift of 3
shift_value = 3
encrypted_content = caesar_cipher_encrypt(content, shift_value)
# Open the destination file in write mode and save the encrypted content
with open('encrypted_output.txt', 'w') as destination_file:
    destination_file.write(encrypted_content)   
print("File content encrypted and saved to encrypted_output.txt") 
