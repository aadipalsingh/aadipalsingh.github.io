'''Remove Empty Sets from List

Problem Statement:
Remove all empty sets from a list of sets.

Input:
[{1, 2}, set(), {3, 4}, set()]

Output:
[{1, 2}, {3, 4}]

'''
# Define the list of sets
list_of_sets = [{1, 2}, set(), {3, 4}, set()]
# Remove empty sets from the list
result = [subset for subset in list_of_sets if subset]  # This will filter out empty sets
# Print the result
print(result)  
# Output: [{1, 2}, {3, 4}]
