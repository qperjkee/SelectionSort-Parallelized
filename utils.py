import numpy as np

def validate_partition_size(data, partition_count) -> bool:
    if len(data) % partition_count != 0:
        print("Error: Cannot divide array into equal partitions with current parameters.")
        return False
    return True

def partition_array(data, partition_count):
    return np.array(data).reshape(partition_count, -1)