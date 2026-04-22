''' Set Difference and Intersection

Problem Statement:
Find the intersection and difference between two sets.

Input:
Set1 = {1, 2, 3, 4}, Set2 = {3, 4, 5, 6}

Output:
Intersection: {3, 4}
Difference: {1, 2}'''
# Define the two sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
# Calculate the intersection
intersection = set1.intersection(set2)
# Calculate the difference (elements in set1 but not in set2)
difference = set1.difference(set2)
# Print the results
print("Intersection:", intersection)  # Output: {3, 4}
print("Difference:", difference)      # Output: {1, 2}