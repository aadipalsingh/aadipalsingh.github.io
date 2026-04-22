'''Tuple Pair Sum

Problem Statement:
Find all pairs in a tuple whose sum equals a given value.

Input:
Tuple = (1, 2, 3, 4, 5), Sum = 5

Output:
[(1, 4), (2, 3)]'''
def find_pairs_with_sum(input_tuple, target_sum):
    pairs = []
    seen = set()
    
    for item in input_tuple:
        complement = target_sum - item
        if complement in seen:
            pairs.append((complement, item))
        seen.add(item)
    
    return pairs
# Example usage
input_tuple = (1, 2, 3, 4, 5)
target_sum = 5
result = find_pairs_with_sum(input_tuple, target_sum)
print(result)  
# Output: [(4, 1), (3, 2)]
