def _linear_search_all_indices(arr, target):
    """
     Modified linear search function to return all indices where target appears.
    
    Args:a
        arr: The list to search in
        target: The value to search for
        
    Returns:
        A list of all indices where the target appears, or an empty list if not found
    """
    indices = []
    for i in range(len(arr)):
        if arr[i] == target:
            indices.append(i)
    return indices


def binary_search_insertion_point(arr, target):
    """
    Uses binary search to find the insertion point for a target value in a sorted list.
    
    Args:
        arr: A sorted list
        target: The value to find the insertion point for
        
    Returns:
        The index where target should be inserted to maintain sorted order
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return left  # This is the insertion point


def linear_search_with_counter(arr, target):
    """
    Linear search that counts the number of comparisons made.
    
    Args:
        arr: The list to search in
        target: The value to search for
        
    Returns:
        A tuple: (index of the target or -1 if not found, number of comparisons)
    """
    comparisons = 0
    for i in range(len(arr)):
        comparisons += 1
        if arr[i] == target:
            return i, comparisons
    return -1, comparisons


def binary_search_with_counter(arr, target):
    """
    Binary search that counts the number of comparisons made.
    
    Args:
        arr: A sorted list to search in
        target: The value to search for
        
    Returns:
        A tuple: (index of the target or -1 if not found, number of comparisons)
    """
    left, right = 0, len(arr) - 1
    comparisons = 0
    
    while left <= right:
        mid = (left + right) // 2
        comparisons += 1
        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1, comparisons


def jump_search(arr, target):
    """
    Jump search algorithm implementation.
    
    Args:
        arr: A sorted list to search in
        target: The value to search for
        
    Returns:
        The index of the target if found, -1 otherwise
    """
    import math
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0
    
    # Finding the block where the element is present
    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1
    
    # Linear search in the identified block
    while arr[prev] < target:
        prev += 1
        if prev == min(step, n):
            return -1
    
    if arr[prev] == target:
        return prev
    
    return -1


def jump_search_with_counter(arr, target):
    """
    Jump search algorithm with comparison counter.
    
    Args:
        arr: A sorted list to search in
        target: The value to search for
        
    Returns:
        A tuple: (index of the target or -1 if not found, number of comparisons)
    """
    import math
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0
    comparisons = 0
    
    # Finding the block where the element is present
    while prev < n and arr[min(step, n) - 1] < target:
        comparisons += 1
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1, comparisons
    
    # Linear search in the identified block
    while prev < n and arr[prev] < target:
        comparisons += 1
        prev += 1
        if prev == min(step, n):
            return -1, comparisons
    
    comparisons += 1  # Final comparison
    if prev < n and arr[prev] == target:
        return prev, comparisons
    
    return -1, comparisons


def compare_search_algorithms_with_counts(arr, target):
    """
    Compare the number of comparisons made by different search algorithms.
    
    Args:
        arr: The list to search in
        target: The value to search for
    """
    import time
    
    # Linear Search
    start_time = time.time()
    linear_result, linear_comparisons = linear_search_with_counter(arr, target)
    linear_time = time.time() - start_time
    
    # Binary Search
    arr_sorted = sorted(arr)
    start_time = time.time()
    binary_result, binary_comparisons = binary_search_with_counter(arr_sorted, target)
    binary_time = time.time() - start_time
    
    # Jump Search
    start_time = time.time()
    jump_result, jump_comparisons = jump_search_with_counter(arr_sorted, target)
    jump_time = time.time() - start_time
    
    print(f"Linear Search: Found at index {linear_result}, Comparisons: {linear_comparisons}, Time: {linear_time:.6f} seconds")
    print(f"Binary Search: Found at index {binary_result}, Comparisons: {binary_comparisons}, Time: {binary_time:.6f} seconds")
    print(f"Jump Search: Found at index {jump_result}, Comparisons: {jump_comparisons}, Time: {jump_time:.6f} seconds")


def main():
    import random
    
    # Create a test list with duplicate values
    test_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print("Original list:", test_list)
    
    # Exercise 1: Find all indices of a target
    target = 5  # Value that appears multiple times
    all_indices = (test_list, target)
    print(f"\nExercise 1: All indices of {target}: {all_indices}")
    
    # Exercise 2: Find insertion point using binary search
    sorted_list = sorted(test_list)
    print("Sorted list:", sorted_list)
    
    target_to_insert = 7
    insertion_point = binary_search_insertion_point(sorted_list, target_to_insert)
    print(f"\nExercise 2: Insertion point for {target_to_insert}: {insertion_point}")
    
    # Exercise 3: Count comparisons in each search algorithm
    print("\nExercise 3: Comparison counts:")
    _, linear_comparisons = linear_search_with_counter(test_list, 6)
    _, binary_comparisons = binary_search_with_counter(sorted_list, 6)
    print(f"Linear search comparisons: {linear_comparisons}")
    print(f"Binary search comparisons: {binary_comparisons}")
    
    # Exercise 4: Implement jump search and compare performance
    print("\nExercise 4: Jump search and performance comparison:")
    large_list = list(range(100000))
    target_large = 99999
    compare_search_algorithms_with_counts(large_list, target_large)
    
    # Demonstrate all exercises with a random list
    print("\n\nDemonstrating all exercises with a random list:")
    random_list = [random.randint(1, 100) for _ in range(20)]
    random_target = random.choice(random_list)
    
    print("Random list:", random_list)
    print(f"Target value: {random_target}")
    
    # Exercise 1: All indices of the target
    all_indices = (random_list, random_target)
    print(f"\nExercise 1: All indices of {random_target}: {all_indices}")
    
    # Exercise 2: Insertion point
    random_sorted = sorted(random_list)
    insert_value = 50
    insertion_point = binary_search_insertion_point(random_sorted, insert_value)
    print(f"\nExercise 2: Insertion point for {insert_value} in sorted list: {insertion_point}")
    print(f"Sorted list: {random_sorted}")
    print(f"After insertion: {random_sorted[:insertion_point] + [insert_value] + random_sorted[insertion_point:]}")
    
    # Exercise 3 & 4: Compare all algorithms with a smaller random list
    print("\nExercises 3 & 4: Compare all search algorithms:")
    compare_search_algorithms_with_counts(random_list, random_target)



main()
