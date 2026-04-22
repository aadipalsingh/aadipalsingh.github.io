'''Find Duplicate Elements in a List

Problem Statement:
Write a program to find all duplicate elements in a given list.

Input:
[1, 2, 3, 2, 4, 5, 1]

Output:
[1, 2]'''
def find_duplicates(input_list):
    duplicates = []
    seen = set()
    
    for item in input_list:
        if item in seen and item not in duplicates:
            duplicates.append(item)
        else:
            seen.add(item)
    
    return duplicates
# Example usage
input_list = [1, 2, 3, 2, 4, 5, 1]
result = find_duplicates(input_list)
print(result)  
# Output: [1, 2]