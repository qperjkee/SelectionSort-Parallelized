import sys
import multiprocessing as mp
from utils import validate_array_division, split_array
from SelectionSort import selection_sort
from Merge import merge_sorted_arrays


def parallel_selection_sort(array: list, num_processes: int) -> list | None:
    if not validate_array_division(array, num_processes):
        sys.exit(1)
    
    chunks = split_array(array, num_processes)
    
    with mp.Pool(processes=num_processes) as pool:
        sorted_chunks = pool.map(selection_sort, chunks)
    
    return merge_sorted_arrays(sorted_chunks)