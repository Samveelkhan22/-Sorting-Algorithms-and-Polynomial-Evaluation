def bubble_sort_modified(arr):
    n = len(arr)
    total_comparisons = 0
    total_swaps = 0

    for i in range(n - 1):
        comparisons = 0
        swaps = 0
        swapped = False

        for j in range(n - 1 - i):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
                swapped = True

        total_comparisons += comparisons
        total_swaps += swaps

        print(f"Iteration {i + 1}: {arr}, Comparisons: {comparisons}, Swaps: {swaps}")

        if not swapped:
            break

    print(f"Total Comparisons: {total_comparisons}, Total Swaps: {total_swaps}")
    return arr

# Test the algorithm on the given instances
A4 = [44, 63, 77, 17, 20, 99, 84, 6, 39, 52]
A5 = [52, 84, 6, 39, 20, 77, 17, 99, 44, 63]
A6 = [6, 17, 20, 39, 44, 52, 63, 77, 84, 99]

print("Sorting A4:")
bubble_sort_modified(A4)
print("\nSorting A5:")
bubble_sort_modified(A5)
print("\nSorting A6:")
bubble_sort_modified(A6)
