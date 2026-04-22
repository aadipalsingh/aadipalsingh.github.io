'''Convert List to Tuple and Remove Duplicates

Problem Statement:
Convert a list into a tuple after removing duplicate elements.

Input:
[1, 2, 2, 3, 4, 4]

Output:
(1, 2, 3, 4)'''
def convert_list_to_tuple(input_list):
    unique_elements = set(input_list)  # Remove duplicates using a set
    return tuple(unique_elements)  # Convert the set back to a tuple
# Example usage
input_list = [1, 2, 2, 3, 4, 4]
result = convert_list_to_tuple(input_list)
print(result)  
# Output: (1, 2, 3, 4)