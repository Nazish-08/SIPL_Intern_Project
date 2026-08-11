import time
import numpy as np


# ============================================================
# 1. SENSOR DATA
# ============================================================

sensor_values = np.array([20, 30, 40, 50, 60])

print("========== SENSOR DATA ==========")
print(sensor_values)


# ============================================================
# 2. VECTORIZED NORMALIZATION
# ============================================================

minimum = sensor_values.min()
maximum = sensor_values.max()

normalized_values = (
    (sensor_values - minimum)
    / (maximum - minimum)
)

print("\n========== NORMALIZED VALUES ==========")
print(normalized_values)


# ============================================================
# 3. NUMPY UFUNCS
# ============================================================

print("\n========== NUMPY UFUNCS ==========")

print("Add 10:", np.add(sensor_values, 10))
print("Subtract 5:", np.subtract(sensor_values, 5))
print("Multiply by 2:", np.multiply(sensor_values, 2))
print("Divide by 2:", np.divide(sensor_values, 2))


# ============================================================
# 4. SENSOR MATRIX
# ============================================================

sensor_matrix = np.array([
    [20, 30, 40],
    [50, 60, 70],
    [80, 90, 100]
])

print("\n========== SENSOR MATRIX ==========")
print(sensor_matrix)

print("Shape:", sensor_matrix.shape)
print("Dimensions:", sensor_matrix.ndim)


# ============================================================
# 5. BROADCASTING
# ============================================================

offset = np.array([1, 2, 3])

broadcasted_result = sensor_matrix + offset

print("\n========== BROADCASTING ==========")
print("Offset:", offset)
print("Result:")
print(broadcasted_result)


# ============================================================
# 6. BOOLEAN MASK
# ============================================================

high_values = sensor_matrix[sensor_matrix > 50]

print("\n========== BOOLEAN MASK ==========")
print("Values greater than 50:")
print(high_values)


# ============================================================
# 7. ROW STATISTICS
# ============================================================

row_mean = np.mean(sensor_matrix, axis=1)
row_std = np.std(sensor_matrix, axis=1)
row_min = np.min(sensor_matrix, axis=1)
row_max = np.max(sensor_matrix, axis=1)

print("\n========== ROW STATISTICS ==========")
print("Row Mean:", row_mean)
print("Row Standard Deviation:", row_std)
print("Row Minimum:", row_min)
print("Row Maximum:", row_max)


# ============================================================
# 8. COLUMN STATISTICS
# ============================================================

column_mean = np.mean(sensor_matrix, axis=0)
column_std = np.std(sensor_matrix, axis=0)
column_min = np.min(sensor_matrix, axis=0)
column_max = np.max(sensor_matrix, axis=0)

print("\n========== COLUMN STATISTICS ==========")
print("Column Mean:", column_mean)
print("Column Standard Deviation:", column_std)
print("Column Minimum:", column_min)
print("Column Maximum:", column_max)


# ============================================================
# 9. GLOBAL STATISTICS
# ============================================================

print("\n========== GLOBAL STATISTICS ==========")

print("Mean:", np.mean(sensor_matrix))
print("Standard Deviation:", np.std(sensor_matrix))
print("Minimum:", np.min(sensor_matrix))
print("Maximum:", np.max(sensor_matrix))


# ============================================================
# 10. PYTHON LOOP CALCULATION
# ============================================================

large_data = np.arange(1, 1_000_001)


start_time = time.perf_counter()

loop_result = []

for value in large_data:
    loop_result.append(value * 2)

loop_time = time.perf_counter() - start_time


# ============================================================
# 11. NUMPY VECTORIZED CALCULATION
# ============================================================

start_time = time.perf_counter()

vectorized_result = large_data * 2

vectorized_time = time.perf_counter() - start_time


# ============================================================
# 12. BENCHMARK COMPARISON
# ============================================================

print("\n========== PERFORMANCE COMPARISON ==========")

print("Python Loop Time:", loop_time, "seconds")
print("NumPy Vectorized Time:", vectorized_time, "seconds")

if vectorized_time > 0:
    speedup = loop_time / vectorized_time
    print("NumPy Speedup:", speedup, "x")


# ============================================================
# 13. VERIFY BOTH RESULTS
# ============================================================

results_match = np.array_equal(
    np.array(loop_result),
    vectorized_result
)

print("\n========== RESULT VERIFICATION ==========")
print("Loop and NumPy results match:", results_match)