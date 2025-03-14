def merge_two_arrays(left: list, right: list) -> list:
    merged = []
    left_index = right_index = 0
    
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    
    if left_index < len(left):
        merged.extend(left[left_index:])
    
    if right_index < len(right):
        merged.extend(right[right_index:])
    
    return merged

def merge_sorted_arrays(arrays: list[list]):
    if len(arrays) == 0:
        return []
    
    if len(arrays) == 1:
        return arrays[0]
    
    if len(arrays) == 2:
        return merge_two_arrays(arrays[0], arrays[1])
    
    middle = len(arrays) // 2
    left_half = merge_sorted_arrays(arrays[:middle])
    right_half = merge_sorted_arrays(arrays[middle:])
    
    return merge_two_arrays(left_half, right_half)