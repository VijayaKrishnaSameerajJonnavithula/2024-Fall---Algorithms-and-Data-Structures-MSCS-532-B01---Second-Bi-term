import random
import time
import tracemalloc

# Quick Sort Implementation
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # Middle element as pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Merge Sort Implementation
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Performance measurement function
def measure_performance(sort_function, data):
    start_time = time.time()  # Start timing
    tracemalloc.start()  # Start memory tracking
    sorted_data = sort_function(data[:])  # Sort a copy of the data to avoid in-place changes
    current, peak = tracemalloc.get_traced_memory()  # Get memory usage
    tracemalloc.stop()  # Stop memory tracking
    end_time = time.time()  # End timing
    
    return {
        "time": end_time - start_time,
        "memory": peak - current
    }

# Prepare datasets
n = 10000  # Size of datasets
datasets = {
    "sorted": list(range(n)),
    "reverse_sorted": list(range(n, 0, -1)),
    "random": [random.randint(0, n) for _ in range(n)],
}

# Running Quick Sort and Merge Sort on each dataset and recording results
results = {}
for dataset_type, dataset in datasets.items():
    print(f"Running tests on {dataset_type} dataset")
    results[dataset_type] = {
        "quick_sort": measure_performance(quick_sort, dataset),
        "merge_sort": measure_performance(merge_sort, dataset)
    }

# Print the results for each dataset type
for dataset_type, metrics in results.items():
    print(f"\nResults for {dataset_type} dataset:")
    for sort_type, performance in metrics.items():
        print(f"{sort_type.capitalize()} - Time: {performance['time']} seconds, Memory: {performance['memory']} bytes")
