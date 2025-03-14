import sys
from utils import validate_array_division, split_array
from Merge import merge_sorted_arrays


def selection_sort(array: list) -> list:
    length = len(array)
    
    for i in range(length - 1):
        min_idx = i
        for j in range(i + 1, length):
            if array[j] < array[min_idx]:
                min_idx = j
                
        if min_idx != i:
            array[i], array[min_idx] = array[min_idx], array[i]
    
    return array

def sort(array: list, num_chunks: int) -> list | None:
    if not validate_array_division(array, num_chunks):
        sys.exit(1)
    
    chunks = split_array(array, num_chunks)
    
    for chunk in chunks:
        selection_sort(chunk)
    
    return merge_sorted_arrays(chunks)

