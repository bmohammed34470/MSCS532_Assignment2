import time
import random

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

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

# Generate datasets
sorted_data = list(range(1000))
reverse_sorted_data = sorted_data[::-1]
random_data = random.sample(range(1000), 1000)

# Performance comparison
def run_algorithm(algorithm, data):
    start_time = time.time()
    algorithm(data)
    end_time = time.time()
    return end_time - start_time

# Run and compare
quick_sort_time_sorted = run_algorithm(quick_sort, sorted_data)
merge_sort_time_sorted = run_algorithm(merge_sort, sorted_data)

quick_sort_time_reverse = run_algorithm(quick_sort, reverse_sorted_data)
merge_sort_time_reverse = run_algorithm(merge_sort, reverse_sorted_data)

quick_sort_time_random = run_algorithm(quick_sort, random_data)
merge_sort_time_random = run_algorithm(merge_sort, random_data)

print(f"Quick Sort - Sorted Data: {quick_sort_time_sorted:.6f} seconds")
print(f"Merge Sort - Sorted Data: {merge_sort_time_sorted:.6f} seconds")
print(f"Quick Sort - Reverse Sorted Data: {quick_sort_time_reverse:.6f} seconds")
print(f"Merge Sort - Reverse Sorted Data: {merge_sort_time_reverse:.6f} seconds")
print(f"Quick Sort - Random Data: {quick_sort_time_random:.6f} seconds")
print(f"Merge Sort - Random Data: {merge_sort_time_random:.6f} seconds")