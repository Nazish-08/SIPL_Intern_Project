import numpy as np


# ============================================================
# 1. 1D ARRAY
# ============================================================

numbers = np.array([10, 20, 30, 40, 50])

print("========== 1D ARRAY ==========")
print(numbers)

print("Shape:", numbers.shape)
print("Dimensions:", numbers.ndim)
print("Data Type:", numbers.dtype)


# ============================================================
# 2. 2D ARRAY
# ============================================================

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("\n========== 2D ARRAY ==========")
print(matrix)

print("Shape:", matrix.shape)
print("Dimensions:", matrix.ndim)
print("Data Type:", matrix.dtype)


# ============================================================
# 3. 3D ARRAY
# ============================================================

cube = np.array([
    [
        [1, 2, 3],
        [4, 5, 6]
    ],
    [
        [7, 8, 9],
        [10, 11, 12]
    ]
])

print("\n========== 3D ARRAY ==========")
print(cube)

print("Shape:", cube.shape)
print("Dimensions:", cube.ndim)
print("Data Type:", cube.dtype)


# ============================================================
# 4. np.arange()
# ============================================================

range_array = np.arange(1, 11)

print("\n========== ARANGE ==========")
print(range_array)


# ============================================================
# 5. np.zeros()
# ============================================================

zero_array = np.zeros((2, 3))

print("\n========== ZEROS ==========")
print(zero_array)


# ============================================================
# 6. np.ones()
# ============================================================

one_array = np.ones((2, 3))

print("\n========== ONES ==========")
print(one_array)


# ============================================================
# 7. RESHAPE
# ============================================================

original_array = np.arange(1, 13)

reshaped_array = original_array.reshape(3, 4)

print("\n========== RESHAPE ==========")

print("Original:")
print(original_array)

print("\nReshaped:")
print(reshaped_array)

print("New Shape:", reshaped_array.shape)


# ============================================================
# 8. INDEXING
# ============================================================

print("\n========== INDEXING ==========")

print("First element:", numbers[0])
print("Third element:", numbers[2])

print("2D element [0, 1]:", matrix[0, 1])
print("2D element [1, 2]:", matrix[1, 2])


# ============================================================
# 9. SLICING
# ============================================================

print("\n========== SLICING ==========")

print("First three elements:", numbers[0:3])
print("Last two elements:", numbers[-2:])

print("\n2D first row:")
print(matrix[0, :])

print("\n2D first two columns:")
print(matrix[:, 0:2])


# ============================================================
# 10. RGB IMAGE REPRESENTATION
# ============================================================

height = 100
width = 200
channels = 3

rgb_image = np.zeros((height, width, channels), dtype=np.uint8)

print("\n========== RGB IMAGE ==========")

print("Image Shape:", rgb_image.shape)
print("Dimensions:", rgb_image.ndim)
print("Data Type:", rgb_image.dtype)

print("Height:", height)
print("Width:", width)
print("Channels:", channels)


# ============================================================
# 11. RGB PIXEL ACCESS
# ============================================================

rgb_image[0, 0] = [255, 0, 0]

print("\nFirst Pixel RGB Value:")
print(rgb_image[0, 0])


# ============================================================
# 12. RGB IMAGE SLICING
# ============================================================

top_left = rgb_image[0:10, 0:10]

print("\nTop Left Image Section Shape:")
print(top_left.shape)