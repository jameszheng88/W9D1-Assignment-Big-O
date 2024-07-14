#  Algorithm 1: Linear Search
#   - Description: Given an unsorted array of integers and a target value, find the index of the first occurrence   of the target value in the array. If the target value is not found, return -1.
#   - Analyze the time complexity of the linear search algorithm and express it using Big O notation.
#   - Implement the linear search algorithm and test it with sample inputs.
#   - Propose an optimization to improve the efficiency of the linear search algorithm, if possible.

def linear_search(arr, target):
    for i in range(len(arr)-1):
        if arr[i] == target:
            return i
    return -1

def linear_search_with_hash_table(arr, target):

    # Create a hash table to map each element to its position

    hash_table = {}
    for i in range(len(arr)):
        hash_table[arr[i]] = i

    if target in hash_table:
        return hash_table[target]
    else:
        return -1

# Sample Test Cases with original
array = [10, 23, 45, 70, 11, 15]
target = 70
print(f"Index of {target}: {linear_search(array, target)}")  # Output: 3

target = 11
print(f"Index of {target}: {linear_search(array, target)}")  # Output: 4

target = 99
print(f"Index of {target}: {linear_search(array, target)}")  # Output: -1

# Sample Test cases with hash table
print(f"Index of {target}: {linear_search_with_hash_table(array, target)}")  # Output: 3

target = 11
print(f"Index of {target}: {linear_search_with_hash_table(array, target)}")  # Output: 4

target = 99
print(f"Index of {target}: {linear_search_with_hash_table(array, target)}")  # Output: -1
