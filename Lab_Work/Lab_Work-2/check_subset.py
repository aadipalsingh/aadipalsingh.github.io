'''Check Subset

Problem Statement:
Check whether one set is a subset of another.

Input:
Set1 = {1, 2}, Set2 = {1, 2, 3, 4}

Output:
True

'''
# Define the two sets
set1 = {1, 2}
set2 = {1, 2, 3, 4}
# Check if set1 is a subset of set2
is_subset = set1.issubset(set2)
# Print the result
print(is_subset)  
# Output: True    
