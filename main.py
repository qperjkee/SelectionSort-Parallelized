import time
from copy import deepcopy
from typing import Callable

from Car import Car
from utils import check_sorted_array


def benchmark_sorting_algorithm(sorting_method: Callable, array_length: int, iterations: int, chunks: int) -> float:

    print("=" * 70)
    print(f"Starting benchmark for {sorting_method.__name__}")
    print(f"Array length: {array_length}, Iterations: {iterations}, Chunks: {chunks}")
    print("-" * 70)
    
    print(f"Creating {array_length} Car objects...")
    original_array = [Car() for _ in range(array_length)]
    
    total_time = 0
    execution_times = []
    
    for i in range(iterations):
        test_array = deepcopy(original_array)
        
        start_time = time.time()
        sorted_array = sorting_method(test_array, chunks)
        end_time = time.time()
        
        execution_time = end_time - start_time
        execution_times.append(execution_time)
        total_time += execution_time
        
        is_sorted = check_sorted_array(sorted_array)
        
        print(f"Iteration {i+1}/{iterations}: {execution_time:.4f} seconds | Sorted correctly: {'✅' if is_sorted else '❌'}")
        
        if not is_sorted:
            print("WARNING: Array not properly sorted!")
    
    avg_time = total_time / iterations
    min_time = min(execution_times)
    max_time = max(execution_times)
    
    print("-" * 70)
    print(f"Benchmark completed for {sorting_method.__name__}")
    print(f"Average time: {avg_time:.4f} seconds")
    print(f"Fastest run: {min_time:.4f} seconds")
    print(f"Slowest run: {max_time:.4f} seconds")
    print("=" * 70)
    
    return avg_time

if __name__ == 'main':
    ...