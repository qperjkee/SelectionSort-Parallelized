import time
from copy import deepcopy
from typing import Callable
import matplotlib.pyplot as plt
import numpy as np

from Car import Car
from utils import check_sorted_array, warm_up_processor
import SelectionSort
import ParallelSelectionSort


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

def run_tests(array_sizes: list[int], iterations: int, chunks: list[int], 
              test_arr_size: bool = True, test_chunks: bool = False, 
              plot_results: bool = True, warm_up: bool = True):
    
    if warm_up:
        warm_up_processor(10000, 10)
    
    default_array_size = array_sizes[0] if test_arr_size else 15000
    default_chunks = chunks[0] if test_chunks else 5
    
    results = {}
    
    if test_arr_size:
        print("\n" + "=" * 40 + " TESTING DIFFERENT ARRAY SIZES " + "=" * 40)
        fixed_chunks = default_chunks
        
        serial_times = []
        parallel_times = []
        
        for size in array_sizes:
            print(f"\n🔍 Testing array size: {size:,} with {fixed_chunks} chunks")
            serial_time = benchmark_sorting_algorithm(SelectionSort.sort, size, iterations, fixed_chunks)
            parallel_time = benchmark_sorting_algorithm(ParallelSelectionSort.parallel_selection_sort, size, iterations, fixed_chunks)
            
            serial_times.append(serial_time)
            parallel_times.append(parallel_time)
        
        speedups = np.divide(serial_times, parallel_times)
        
        results['array_sizes'] = {
            'sizes': array_sizes,
            'serial': serial_times,
            'parallel': parallel_times,
            'speedup': speedups
        }

        print_test_results(array_sizes, serial_times, parallel_times, speedups, label="Array Size")
        
    if test_chunks:
        print("\n" + "=" * 40 + " TESTING DIFFERENT CHUNK COUNTS " + "=" * 40)
        fixed_size = default_array_size
        
        serial_times = []
        parallel_times = []
        
        for chunk_count in chunks:
            print(f"\n🔍 Testing chunk count: {chunk_count:,} with array size {fixed_size:,}")
            serial_time = benchmark_sorting_algorithm(SelectionSort.sort, fixed_size, iterations, chunk_count)
            parallel_time = benchmark_sorting_algorithm(ParallelSelectionSort.parallel_selection_sort, fixed_size, iterations, chunk_count)
            
            serial_times.append(serial_time)
            parallel_times.append(parallel_time)
        
        speedups = np.divide(serial_times, parallel_times)
        
        results['chunks'] = {
            'counts': chunks,
            'serial': serial_times,
            'parallel': parallel_times,
            'speedup': speedups
        }

        print_test_results(chunks, serial_times, parallel_times, speedups, label="Chunk Count")

    if plot_results and (test_arr_size or test_chunks):
        plot_test_results(results, test_arr_size, test_chunks)
    
    return results

def print_test_results(array_sizes, serial_times, parallel_times, speedups, label="Array Size"):
    print("\n📊 Results of testing:")
    header = f"+{'-'*16}+{'-'*12}+{'-'*13}+{'-'*10}+"
    print(header)
    print("| {:15s} | {:11s} | {:12s} | {:9s} |".format(label, "Serial (s)", "Parallel (s)", "Speedup"))
    print(header)
    
    for i, size in enumerate(array_sizes):
        print("| {:15d} | {:11.2f} | {:12.2f} | {:9.3f} |".format(
            size, serial_times[i], parallel_times[i], speedups[i]))
    
    print(header)

def plot_test_results(results, test_arr_size, test_chunks):
    plt.figure(figsize=(16, 10))
    
    if test_arr_size and 'array_sizes' in results:
        data = results['array_sizes']
        
        plt.subplot(1, 2, 1)
        plt.plot(data['sizes'], data['serial'], 'b-o', label='Serial')
        plt.plot(data['sizes'], data['parallel'], 'r-o', label='Parallel')
        plt.xlabel('Array Size')
        plt.ylabel('Time (s)')
        plt.title('Execution Time vs Array Size')
        plt.legend()
        plt.grid(True)
        
        plt.subplot(1, 2, 2)
        plt.plot(data['sizes'], data['speedup'], 'g-o')
        plt.xlabel('Array Size')
        plt.ylabel('Speedup (Serial/Parallel)')
        plt.title('Speedup vs Array Size')
        plt.grid(True)
    
    if test_chunks and 'chunks' in results:
        data = results['chunks']
        
        plt.subplot(1, 2, 1)
        plt.plot(data['counts'], data['serial'], 'b-o', label='Serial')
        plt.plot(data['counts'], data['parallel'], 'r-o', label='Parallel')
        plt.xlabel('Number of Chunks')
        plt.ylabel('Time (s)')
        plt.title('Execution Time vs Number of Chunks')
        plt.legend()
        plt.grid(True)
        
        plt.subplot(1, 2, 2)
        plt.plot(data['counts'], data['speedup'], 'g-o')
        plt.xlabel('Number of Chunks')
        plt.ylabel('Speedup (Serial/Parallel)')
        plt.title('Speedup vs Number of Chunks')
        plt.grid(True)
    
    plt.tight_layout()
    plt.savefig('sorting_results.png')
    plt.show()


def main():
    run_tests(array_sizes=[1000, 2500, 5000, 10000, 15000, 20000, 25000], iterations=10, chunks=[1, 2, 5, 10, 20, 25, 50],
              test_arr_size=False, test_chunks=True, plot_results=True, warm_up=True)

if __name__ == '__main__':
    main()