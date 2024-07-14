# Algorithm 2: Bubble Sort
   # - Description: Given an unsorted array of integers, sort the array in ascending order using the bubble sort algorithm.
   # - Analyze the time complexity of the bubble sort algorithm and express it using Big O notation.
   # - Implement the bubble sort algorithm and test it with sample inputs.
   # - Identify the inefficiencies in the bubble sort algorithm and propose an optimized version of the algorithm.
def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range (len(arr)-1):
            if arr[j] > arr [j + 1]:
                [arr[j], arr[j+1]] = [arr[j+1], arr[j]]
    return arr

def bubble_sort_with_flag(arr):
    # Traverse through all array elements
    for i in range(len(arr)):

        # Keep track of swapping
        swapped = False

        # Loop to compare array elements
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j+1]:

                # swapping occurs if elements are not in the intended order
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if (swapped == False):
            break

    return arr


# Sample Test Cases with original bubble sort
array = [64, 34, 25, 12, 22, 11, 90]
print(f"Sorted array: {bubble_sort(array)}")  # Output: [11, 12, 22, 25, 34, 64, 90]

array = [5, 1, 4, 2, 8]
print(f"Sorted array: {bubble_sort(array)}")  # Output: [1, 2, 4, 5, 8]

# Sample Test Cases with flag variable
array = [64, 34, 25, 12, 22, 11, 90]
print(f"Sorted array: {bubble_sort_with_flag(array)}")  # Output: [11, 12, 22, 25, 34, 64, 90]

array = [5, 1, 4, 2, 8]
print(f"Sorted array: {bubble_sort_with_flag(array)}")  # Output: [1, 2, 4, 5, 8]