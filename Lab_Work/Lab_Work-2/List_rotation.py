'''List Rotation

Problem Statement:
Rotate a list to the right by k positions.

Input:
List = [10, 20, 30, 40, 50], k = 2

Output:
[40, 50, 10, 20, 30]'''
def rotate_list(input_list, k):
    k = k % len(input_list)  # Handle cases where k is greater than the list length
    return input_list[-k:] + input_list[:-k]
# Example usage
input_list = [10, 20, 30, 40, 50]
k = 2
result = rotate_list(input_list, k)
print(result)  
# Output: [40, 50, 10, 20, 30]