**Merge Sort using Divide and Conquer**

**1. Objective**

To develop a Python-based Merge Sort program using the Divide and Conquer technique and calculate its time complexity.

**2. Input**

The program accepts:

Number of elements in the array

Elements of the array

**3. Output**

The program displays:

Original array

Sorted array

Time complexity

Best case: O(n log n)

Average case: O(n log n)

Worst case: O(n log n)

**4. Algorithm**

Start.

Read the number of elements in the array.

Read the elements of the array.

Apply Merge Sort:

Divide:

Find the middle position of the array.

Divide the array into two halves.

Conquer:

Recursively apply Merge Sort to the left half.

Recursively apply Merge Sort to the right half.

Combine:

Compare elements from both sorted halves.

Merge them into a single sorted array.

If the array contains zero or one element, return the array because it is already sorted.

Display the original array.

Display the sorted array.

Calculate the time complexity of Merge Sort.

The recurrence relation is:

T(n) = 2T(n/2) + O(n)

Therefore, the time complexity is:

Best Case = O(n log n)

Average Case = O(n log n)

Worst Case = O(n log n)

Stop.

**5. Time Complexity**

O(n log n)

Where n is the number of elements in the array.

Merge Sort divides the array into two halves recursively. The merging process takes O(n) time at each level.

There are O(log n) levels of division.

Therefore, the overall time complexity is O(n log n) for the best, average, and worst cases.
 
