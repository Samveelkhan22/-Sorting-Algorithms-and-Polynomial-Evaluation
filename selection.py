def selection_sort_modified(arr):
    n = len(arr)
    for i in range(n):
        # Initialize the counters for comparisons and swaps
        comparisons = 0
        swaps = 0
        
        # Find the maximum element in the unsorted portion of the array
        max_index = 0
        for j in range(1, n - i):
            comparisons += 1
            if arr[j] > arr[max_index]:
                max_index = j

        # Swap the found maximum element with the element at its correct position
        arr[max_index], arr[n - 1 - i] = arr[n - 1 - i], arr[max_index]
        swaps += 1
        
        # Print the partially sorted array, number of comparisons, and number of swaps
        print(f"Iteration {i + 1}: {arr}, Comparisons: {comparisons}, Swaps: {swaps}")

    return arr

# Test the algorithm on the given instances
A1 = [63, 44, 17, 77, 20, 6, 99, 84, 52, 39]
A2 = [84, 52, 39, 6, 20, 17, 77, 99, 63, 44]
A3 = [99, 84, 77, 63, 52, 44, 39, 20, 17, 6]

print("Sorting A1:")
selection_sort_modified(A1)
print("\nSorting A2:")
selection_sort_modified(A2)
print("\nSorting A3:")
selection_sort_modified(A3)
