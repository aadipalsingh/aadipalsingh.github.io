'''Tail Implementation (Like Linux tail)
 Display last N lines of a file efficiently.

'''
def tail(file_path, n):
    with open(file_path, 'r') as file:
        # Move the pointer to the end of the file
        file.seek(0, 2)
        file_size = file.tell()
        buffer_size = 1024
        buffer = ''
        lines = []
        
        # Read the file in reverse until we have enough lines
        while len(lines) < n and file_size > 0:
            # Calculate how much to read
            read_size = min(buffer_size, file_size)
            file.seek(file_size - read_size)
            buffer = file.read(read_size) + buffer
            file_size -= read_size
            
            # Split the buffer into lines
            lines = buffer.splitlines()
        
        # Return the last N lines
        return lines[-n:]   
# Example usage
if __name__ == "__main__":
    file_path = 'input.txt'  # Replace with your file path
    n = 10  # Number of lines to display
    last_lines = tail(file_path, n)
    print("\n".join(last_lines))    
    