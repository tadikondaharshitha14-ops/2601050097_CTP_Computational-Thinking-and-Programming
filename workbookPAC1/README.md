# Merge Sort using Divide and Conquer 

def merge_sort(arr):

    # Base condition
    if len(arr) <= 1:
        return arr

    # Divide
    mid = len(arr) // 2

    left = arr[:mid]
    right = arr[mid:]

    # Conquer
    left = merge_sort(left)
    right = merge_sort(right)

    # Combine
    return merge(left, right)


def merge(left, right):

    result = []
    i = 0
    j = 0

    # Compare elements and merge
    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])

    return result


# Input
arr = [38, 12, 27, 43, 9, 31, 18, 25]

print("Original array:", arr)

sorted_arr = merge_sort(arr)

print("Sorted array:", sorted_arr)
