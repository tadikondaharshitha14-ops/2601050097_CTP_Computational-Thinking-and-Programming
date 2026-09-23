def merge_sort(arr):

    # Base condition
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = arr[:mid]
    right = arr[mid:]


    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)
