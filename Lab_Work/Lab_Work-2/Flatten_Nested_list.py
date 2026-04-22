'''Flatten Nested List

Problem Statement:
Flatten a nested list (1 level deep).

Input:
[[1, 2], [3, 4], [5]]

Output:
[1, 2, 3, 4, 5]'''
def flatten_nested_list(nested_list):
    flattened_list = []
    for sublist in nested_list:
        flattened_list.extend(sublist)  # Extend the flattened list with the elements of the sublist
    return flattened_list
# Example usage
nested_list = [[1, 2], [3, 4], [5]]
result = flatten_nested_list(nested_list)
print(result)  
# Output: [1, 2, 3, 4, 5]
