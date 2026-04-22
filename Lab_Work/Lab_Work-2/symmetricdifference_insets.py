'''Symmetric Difference of Sets

Problem Statement:
Find elements that are in either of the sets but not in both.

Input:
Set1 = {1, 2, 3}, Set2 = {3, 4, 5}

Output:
{1, 2, 4, 5}

'''
# Define the two sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
# Calculate the symmetric difference
sd = set1.symmetric_difference(set2)
# Print the result
print(sd)  
# Output: {1, 2, 4, 5}