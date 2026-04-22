'''Merge and Sort Unique Elements

Problem Statement:
Merge two lists and return a sorted list of unique elements.

Input:
[3, 1, 2], [2, 4, 5]

Output:
[1, 2, 3, 4, 5]

'''
def merge_and_sort_unique(list1, list2):
    # Merge the two lists
    merged_list = list1 + list2
    
    # Remove duplicates by converting to a set, then back to a list
    unique_elements = list(set(merged_list))
    
    # Sort the list of unique elements
    unique_elements.sort()
    
    return unique_elements
# Example usage
list1 = [3, 1, 2]
list2 = [2, 4, 5]
result = merge_and_sort_unique(list1, list2)
print(result)  
# Output: [1, 2, 3, 4, 5]   
