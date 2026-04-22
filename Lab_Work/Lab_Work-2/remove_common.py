'''Remove Common Elements from Two Lists

Problem Statement:
Remove elements from the first list that are present in the second list.

Input:
List1 = [1, 2, 3, 4], List2 = [3, 4, 5]

Output:
[1, 2]'''
#to remove common elements from the following lists
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5]

result = list(set(list1) - set(list2))

print(result)
# Output: [1, 2]
