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