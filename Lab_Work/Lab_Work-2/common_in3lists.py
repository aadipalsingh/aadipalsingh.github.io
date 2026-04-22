'''Common Elements in Three Lists

Problem Statement:
Find common elements present in three lists.

Input:
[1, 2, 3], [2, 3, 4], [2, 5, 3]

Output:
[2, 3]'''
def common_elements(list1, list2, list3):
    # Convert lists to sets and find the intersection
    set1 = set(list1)
    set2 = set(list2)
    set3 = set(list3)
    
    common = set1.intersection(set2).intersection(set3)
    
    return list(common)
# Example usage
list1 = [1, 2, 3]
list2 = [2, 3, 4]
list3 = [2, 5, 3]
result = common_elements(list1, list2, list3)
print(result)  
# Output: [2, 3]
