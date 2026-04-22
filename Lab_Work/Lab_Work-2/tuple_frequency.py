'''Tuple Element Frequency

Problem Statement:
Count the frequency of each element in a tuple.

Input:
(1, 2, 2, 3, 1, 4)

Output:
{1: 2, 2: 2, 3: 1, 4: 1}'''
def count_frequency(input_tuple):
    frequency = {}
    
    for item in input_tuple:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
            
    return frequency
# Example usage
input_tuple = (1, 2, 2, 3, 1, 4)
result = count_frequency(input_tuple)
print(result)  
# Output: {1: 2, 2: 2, 3: 1, 4: 1}