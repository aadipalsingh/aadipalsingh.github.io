'''Find Maximum and Minimum in Tuple

Problem Statement:
Find the maximum and minimum elements in a tuple without using built-in functions.

Input:
(5, 1, 8, 3)

Output:
Max = 8, Min = 1

'''
def find_max_min(input_tuple):
    if not input_tuple:
        return None, None  # Handle empty tuple case
    
    max_value = input_tuple[0]
    min_value = input_tuple[0]
    
    for item in input_tuple:
        if item > max_value:
            max_value = item
        if item < min_value:
            min_value = item
            
    return max_value, min_value
# Example usage
input_tuple = (5, 1, 8, 3)
max_value, min_value = find_max_min(input_tuple)
print(f'Max = {max_value}, Min = {min_value}')  
# Output: Max = 8, Min = 1  
