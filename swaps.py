def min_swaps_to_convert(list1, list2):
    # Step 1: Create a dictionary to store the index of elements in list2
    n = len(list1)
    index_map = {value: idx for idx, value in enumerate(list2)}
    
    # Step 2: Initialize an array to mark visited elements
    visited = [False] * n
    
    # Step 3: Count swaps by traversing cycles
    swap_count = 0
    
    for i in range(n):
        # If element is already visited or already in the correct position, skip it
        if visited[i] or list1[i] == list2[i]:
            continue
        
        # Find the cycle size
        cycle_size = 0
        j = i
        
        while not visited[j]:
            visited[j] = True
            j = index_map[list1[j]]  # Move to the next element in the cycle
            cycle_size += 1
        
        # If there is a cycle of size `cycle_size`, we need `cycle_size - 1` swaps
        if cycle_size > 1:
            swap_count += (cycle_size - 1)
    
    return swap_count

# Example usage
list1 = [18, 6, 13, 3, 2, 5, 7, 9, 17, 11, 1, 8, 12, 0, 15, 4, 10, 14, 16]
list2 = [8, 9, 6, 17, 13, 18, 12, 16, 5, 10, 3, 4, 11, 7, 14, 15, 0, 1, 2]

swaps = min_swaps_to_convert(list1, list2)
print(f"Number of swaps required: {swaps}")
