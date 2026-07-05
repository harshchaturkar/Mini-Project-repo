'''# Q1. Array Properties
import numpy as np

array = np.random.randint(10, 101, size=(5, 6))

print("Array:")
print(array)

print("\nShape of the array:", array.shape)
print("Total number of elements (size):", array.size)
print("Data type (dtype):", array.dtype)'''










'''# Q2. Statistical Methods - Basic
import numpy as np

array = np.random.randint(1, 51, 20)

print("Array:")
print(array)

print("\nMinimum value:", np.min(array))
print("Index of minimum value:", np.argmin(array))

print("\nMaximum value:", np.max(array))
print("Index of maximum value:", np.argmax(array))

print("\nSum of all elements:", np.sum(array))

print("Mean:", np.mean(array))
print("Standard Deviation:", np.std(array))'''










'''# Q3. Statistical Methods on 2D Array
import numpy as np

matrix = np.random.randint(20, 81, (4, 5))

print("Matrix:")
print(matrix)

print("\nMinimum value:", np.min(matrix))
print("Maximum value:", np.max(matrix))
print("Sum of all elements:", np.sum(matrix))
print("Mean:", np.mean(matrix))
print("Standard Deviation:", np.std(matrix))

print("\nSum of each row:")
print(np.sum(matrix, axis=1))

print("\nSum of each column:")
print(np.sum(matrix, axis=0))'''









'''# Q4. Reshape
import numpy as np

array = np.arange(1, 25)

print("Original 1D Array:")
print(array)
print("Shape:", array.shape)

# Reshape into (4, 6)
array1 = array.reshape(4, 6)
print("\nReshaped to (4, 6):")
print(array1)
print("Shape:", array1.shape)

# Reshape into (3, 8)
array2 = array.reshape(3, 8)
print("\nReshaped to (3, 8):")
print(array2)
print("Shape:", array2.shape)

# Reshape into (2, 3, 4)
array3 = array.reshape(2, 3, 4)
print("\nReshaped to (2, 3, 4):")
print(array3)
print("Shape:", array3.shape)'''










'''# Q5. NumPy Indexing - 1D & 2D
import numpy as np

arr = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120]
])

print("Original Array:")
print(arr)

print("\nFirst Row:")
print(arr[0])

print("\nLast Column:")
print(arr[:, -1])

print("\nCenter 2x2 Submatrix:")
print(arr[1:3, 1:3])

print("\nEven Numbers:")
print(arr[arr % 2 == 0])
'''










'''# Q6. Advanced Indexing
import numpy as np

arr = np.random.randint(1, 101, (5, 5))

print("Original Array:")
print(arr)

print("\nDiagonal Elements:")
print(np.diag(arr))

print("\nElements Greater Than 50:")
print(arr[arr > 50])

arr[arr < 30] = 0

print("\nModified Array (Elements < 30 replaced with 0):")
print(arr)'''











'''# Q7. Arithmetic Operations
import numpy as np

a = np.array([10, 20, 30, 40])
b = np.array([1, 2, 3, 4])

print("Array a:", a)
print("Array b:", b)

# Addition
print("\nAddition:")
print(a + b)
# Subtraction
print("\nSubtraction:")
print(a - b)
# Multiplication
print("\nMultiplication:")
print(a * b)
# Division
print("\nDivision:")
print(a / b)

# Element-wise Power
print("\nElement-wise Power (a ** b):")
print(a ** b)

# Modulo Operation
print("\nModulo Operation (a % b):")
print(a % b)'''











'''# Q8. Matrix Multiplication
import numpy as np

A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

B = np.array([
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
])

print("Matrix A:")
print(A)
print("\nMatrix B:")
print(B)

elementwise = A * B
print("\nElement-wise Multiplication:")
print(elementwise)

matrix_mul = A @ B      
print("\nMatrix Multiplication:")
print(matrix_mul)

# Difference:
# A * B multiplies corresponding elements of the two matrices.
# A @ B (or np.dot(A, B)) performs matrix multiplication
# using rows of A and columns of B.'''










'''# Q9. Combined - Properties + Operations + Indexing
import numpy as np

matrix = np.random.randn(6, 6)

print("Original Matrix:")
print(matrix)

print("\nShape:", matrix.shape)
print("Size:", matrix.size)
print("Data Type:", matrix.dtype)

print("\nMaximum Value:", np.max(matrix))
print("Index of Maximum Value:", np.argmax(matrix))

print("\nMinimum Value:", np.min(matrix))
print("Index of Minimum Value:", np.argmin(matrix))

print("\nTop-Left 3x3 Submatrix:")
print(matrix[:3, :3])

matrix = np.abs(matrix)

print("\nModified Matrix (Negative values converted to positive):")
print(matrix)

print("\nMean of Modified Matrix:", np.mean(matrix))'''











# Q10. Mini Project - Student Performance Analysis
import numpy as np

marks = np.random.randint(30, 101, (10, 5))

print("Student Marks:")
print(marks)

# Calculate total marks of each student
total = np.sum(marks, axis=1)
print("\nTotal Marks:")
print(total)

# Calculate average marks of each student
average = np.mean(marks, axis=1)
print("\nAverage Marks:")
print(average)

# Find student with highest total marks
highest = np.argmax(total)
print("\nStudent with Highest Total:", highest + 1)
print("Total Marks:", total[highest])

# Find student with lowest total marks
lowest = np.argmin(total)
print("\nStudent with Lowest Total:", lowest + 1)
print("Total Marks:", total[lowest])

# Calculate overall class mean and standard deviation
print("\nClass Mean:", np.mean(marks))
print("Class Standard Deviation:", np.std(marks))

# Extract marks of top 3 students
top3 = np.argsort(total)[-3:]

print("\nTop 3 Students (Student Numbers):")
print(top3 + 1)

print("\nMarks of Top 3 Students:")
print(marks[top3])