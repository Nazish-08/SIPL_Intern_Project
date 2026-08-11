# Vectorization and Broadcasting

## Description
This project demonstrates NumPy vectorization, broadcasting, boolean masking and statistical operations using sensor data. It also compares the execution time of a Python loop with a NumPy vectorized operation.

## Features
- Normalize sensor values using vectorized operations
- Apply NumPy universal functions (ufuncs)
- Demonstrate broadcasting
- Filter data using boolean masks
- Calculate row and column statistics
- Calculate mean, standard deviation, minimum and maximum
- Compare Python loop and NumPy execution time
- Verify that both approaches produce the same result

## File

- vectorization_benchmark.py

## Concepts Used

- Vectorization
- Broadcasting
- NumPy ufuncs
- Boolean masks
- mean()
- std()
- min()
- max()
- axis
- Performance benchmarking

## How to Run

```bash
python vectorization_benchmark.py
```

## Output

The program displays:

- Original sensor values
- Normalized sensor values
- Broadcasting results
- Boolean mask results
- Row and column statistics
- Python loop execution time
- NumPy vectorized execution time
- NumPy speedup
- Result verification

## Learning Outcome

- Learned how vectorization replaces explicit Python loops.
- Understood how NumPy broadcasting applies operations across compatible array dimensions.
- Practiced boolean masking and statistical operations.
- Compared Python loop performance with NumPy vectorized operations.