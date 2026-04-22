'''Tuple to Dictionary Mapping

Problem Statement:
Convert two tuples into a dictionary where one tuple contains keys and the other contains values.

Input:
Keys = ('a', 'b', 'c'), Values = (1, 2, 3)

Output:
{'a': 1, 'b': 2, 'c': 3}'''
def tuples_to_dictionary(keys_tuple, values_tuple):
    if len(keys_tuple) != len(values_tuple):
        raise ValueError("Both tuples must have the same length.")
    
    return dict(zip(keys_tuple, values_tuple))
# Example usage
keys_tuple = ('a', 'b', 'c')
values_tuple = (1, 2, 3)
result = tuples_to_dictionary(keys_tuple, values_tuple)
print(result)  
# Output: {'a': 1, 'b': 2, 'c': 3}
