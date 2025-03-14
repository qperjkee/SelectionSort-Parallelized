import numpy as np
import Car
import SelectionSort

def validate_partition_size(data: list, partition_count: int) -> bool:
    if len(data) % partition_count != 0:
        print("Error: Cannot divide array into equal partitions with current parameters.")
        return False
    return True

def split_array(data: list, partition_count: int):
    return np.array(data).reshape(partition_count, -1)

def check_sorted_array(array: list) -> bool:
    for i in range(len(array) - 1):
        if array[i + 1] < array[i]:
            return False
    return True

def warm_up_processor(array_size: int, iterations: int):
    print("=" * 50)
    print("Starting CPU warm-up process...")
    print(f"Creating an array of {array_size} 'Car' objects for testing.")
    array = [Car() for _ in range(array_size)]
    
    print(f"Performing {iterations} iterations of sorting...")
    for i in range(iterations):
        SelectionSort.sort(array, 5)
        print(f"  ✔️ Iteration {i + 1} completed successfully.")
    
    print("Warming up process completed.")
    print("=" * 50)