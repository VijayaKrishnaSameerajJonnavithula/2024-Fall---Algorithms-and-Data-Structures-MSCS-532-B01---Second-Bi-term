def insertion_sort_descending(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Move elements of arr[0...i-1] that are less than key
        # to one position ahead of their current position
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Example usage:
arr = [20, 201, 113, 15, 66]
sorted_arr = insertion_sort_descending(arr)
print("Sorted array in descending order:", sorted_arr)
