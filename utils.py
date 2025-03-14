import numpy as np


def validate_partition_size(data: list, partition_count: int) -> bool:
    if len(data) % partition_count != 0:
        print("Error: Cannot divide array into equal partitions with current parameters.")
        return False
    return True

def split_array(data: list, partition_count: int):
    return np.array(data).reshape(partition_count, -1)