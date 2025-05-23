# Parallel Selection Sort Benchmark

This project implements and compares the performance of serial and parallel versions of the Selection Sort algorithm using Python's multiprocessing capabilities.

## Project Overview

The project evaluates the efficiency of parallelizing the Selection Sort algorithm by dividing arrays into chunks, sorting them independently, and then merging the results. It includes comprehensive benchmarking tools to measure and visualize performance differences across various array sizes and chunk configurations.

## Components

### Core Sorting Implementation
- **SelectionSort.py**: Contains the classic Selection Sort algorithm implementation and a chunked version that splits arrays before sorting
- **ParallelSelectionSort.py**: Implements a parallel version using Python's multiprocessing library
- **Merge.py**: Provides efficient merging algorithms for combining sorted arrays

### Data Model
- **Car.py**: Defines a `Car` class with randomized attributes (engine power, max speed, fuel consumption) that serves as the test data type with custom comparison operators

### Testing Infrastructure
- **utils.py**: Utility functions for array manipulation, validation, and CPU warm-up
- **main.py**: Benchmarking framework that runs experiments and generates visualizations

## How It Works

### Selection Sort Algorithm
The implementation follows the standard Selection Sort approach:
1. Find the minimum element in the unsorted portion of the array
2. Swap it with the element at the current position
3. Move to the next position and repeat

![Image](https://github.com/user-attachments/assets/2190d71e-d222-4bdf-bcf4-648f80ebb089)

### Parallelization Approach
The parallel version:
1. Divides the input array into equal chunks
2. Processes each chunk independently using a separate process
3. Merges the sorted chunks using a hierarchical merge algorithm

![Image](https://github.com/user-attachments/assets/e976b1db-f348-4ecf-88e5-33ba10f3c7f9)

### Benchmarking Methodology
The benchmarking system:
1. Creates arrays of `Car` objects with random attributes
2. Runs multiple iterations of both algorithms for statistical significance
3. Measures execution time and validates correct sorting
4. Calculates speedup (ratio of serial to parallel execution time)
5. Generates plots to visualize performance characteristics

## Test Parameters

Two primary experiments are conducted:

### Array Size Test
Evaluates how performance scales with increasing array sizes while keeping the number of chunks constant.
- Array sizes: 1,000, 2,500, 5,000, 10,000, 15,000, 20,000, 25,000
- Fixed number of chunks: 5
- Iterations per test: 10

### Chunk Count Test
Examines the impact of different chunk counts (parallelism levels) on a fixed-size array.
- Fixed array size: 15,000
- Chunk counts: 1, 2, 5, 10, 20, 25, 50
- Iterations per test: 10

## Key Features

- **Processor Warm-up**: Runs preliminary sorts to ensure CPU caching is stabilized before benchmarking
- **Deep Copying**: Ensures identical test data across iterations
- **Verification**: Checks that arrays are properly sorted after each operation
- **Statistical Analysis**: Tracks minimum, maximum, and average execution times
- **Data Visualization**: Generates comparative plots for execution time and speedup

## Results Visualization

The benchmarking process generates two types of plots:
1. **Execution Time vs. Parameter**: Compares serial and parallel execution times
2. **Speedup vs. Parameter**: Shows the performance improvement factor

![Image](https://github.com/user-attachments/assets/2095b679-9bf9-4566-a206-ec5918c7b22a)
![Image](https://github.com/user-attachments/assets/82a8e6dd-02bd-46ca-a619-e148d1bbe6b5)

## Usage

To run the benchmarks:

```python
python main.py
```

You can modify the test parameters in the main() function inside main.py:
```python
run_tests(
    array_sizes=[1000, 2500, 5000, 10000, 15000, 20000, 25000], 
    iterations=10, 
    chunks=[1, 2, 5, 10, 20, 25, 50],
    test_arr_size=False,  # Set to True to test different array sizes
    test_chunks=True,     # Set to True to test different chunk counts
    plot_results=True,    # Set to True to generate plots
    warm_up=True          # Set to True to perform processor warm-up
)
```

## Requirements

- Python 3.9+
- NumPy
- Matplotlib
- Multiprocessing (standard library)

## Expected Outcomes

The project demonstrates several key principles of parallel algorithm design:
1. For small arrays, overhead may outweigh performance benefits
2. Beyond certain sizes, parallel processing shows significant speedup
3. Optimal chunk count depends on hardware characteristics and problem size
