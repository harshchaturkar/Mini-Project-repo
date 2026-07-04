''' # Q.1)
import numpy as np

# a) Create a 1D array
array1 = np.array([10, 20, 30, 40, 50])
# Print 1D array
print("1D Array:")
print(array1)
print("Shape:", array1.shape)
print("Data Type:", array1.dtype)

# b) Create a 3x3 (2D) array
array2 = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
# Print 2D array
print("2D Array:")
print(array2)
print("Shape:", array2.shape)
print("Data Type:", array2.dtype)'''






'''# Q.2)
import numpy as np

# a) Create a 1D array of 8 zeros
array1 = np.zeros(8)

# b) Create a 4x4 array filled with ones
array2 = np.ones((4, 4))

# c) Create a 3x3 matrix of zeros
array3 = np.zeros((3, 3))

# Print all arrays with labels
print("a) 1D Array of 8 Zeros:")
print(array1)

print("\nb) 4x4 Array of Ones:")
print(array2)

print("\nc) 3x3 Matrix of Zeros:")
print(array3)'''







'''# Q.3)
import numpy as np

# a) Numbers from 0 to 20 (step 1)
array1 = np.arange(0, 21, 1)

# b) Even numbers from 10 to 50
array2 = np.arange(10, 51, 2)

# c) Numbers from 5 to 100 with step of 5
array3 = np.arange(5, 101, 5)

# Print the arrays
print("a) Numbers from 0 to 20:")
print(array1)

print("\nb) Even numbers from 10 to 50:")
print(array2)

print("\nc) Numbers from 5 to 100 (step of 5):")
print(array3)'''









'''# Q.4)
import numpy as np

# a) 10 equally spaced numbers between 0 and 5
array1 = np.linspace(0, 5, 10)

# b) 15 equally spaced numbers between -10 and 10
array2 = np.linspace(-10, 10, 15)

# Print the arrays and their lengths
print("a) 10 equally spaced numbers between 0 and 5:")
print(array1)
print("Length:", len(array1))

print("\nb) 15 equally spaced numbers between -10 and 10:")
print(array2)
print("Length:", len(array2))'''









'''# Q.5)
import numpy as np

# a) 1D array of 10 random numbers between 0 and 1
array1 = np.random.rand(10)

# b) 3x3 matrix of random numbers from standard normal distribution
array2 = np.random.randn(3, 3)

# c) 4x5 array of random integers between 10 and 50
array3 = np.random.randint(10, 51, (4, 5))

# Print the arrays
print("a) 1D Array of 10 Random Numbers (0 to 1):")
print(array1)

print("\nb) 3x3 Matrix of Random Numbers (Standard Normal Distribution):")
print(array2)

print("\nc) 4x5 Array of Random Integers (10 to 50):")
print(array3)'''









'''# Q.6)
import numpy as np

# Create two vectors
v1 = np.array([2, 4, 6, 8])
v2 = np.array([1, 3, 5, 7])

# Addition
addition = v1 + v2

# Subtraction
subtraction = v1 - v2

# Element-wise multiplication
multiplication = v1 * v2

# Dot product
dot_product = np.dot(v1, v2)

# Print the results
print("Vector 1:", v1)
print("Vector 2:", v2)
print("\nAddition:")
print(addition)
print("\nSubtraction:")
print(subtraction)
print("\nElement-wise Multiplication:")
print(multiplication)
print("\nDot Product:")
print(dot_product)'''








'''# Q.7)
import numpy as np
# Create two 3x3 matrices
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

B = np.array([[9, 8, 7],
              [6, 5, 4],
              [3, 2, 1]])

# Matrix Addition
addition = A + B
# Matrix Multiplication
multiplication = A @ B
# Element-wise Multiplication
element_wise = A * B

# Print the results
print("Matrix A:")
print(A)
print("\nMatrix B:")
print(B)
print("\nMatrix Addition:")
print(addition)
print("\nMatrix Multiplication:")
print(multiplication)
print("\nElement-wise Multiplication:")
print(element_wise)'''










'''# Q.8)
import numpy as np

# Create a 4x4 matrix of random integers between 1 and 100
matrix = np.random.randint(1, 101, (4, 4))

# Print the matrix
print("4x4 Random Matrix:")
print(matrix)

# Print properties
print("\nShape:", matrix.shape)
print("Dimension (ndim):", matrix.ndim)
print("Total Number of Elements (size):", matrix.size)
print("Data Type (dtype):", matrix.dtype)
print("Minimum Value:", matrix.min())
print("Maximum Value:", matrix.max())'''









'''Q.9)
import numpy as np

# Generate a 1D array of 20 random integers between 1 and 50
array = np.random.randint(1, 51, 20)

# Reshape into a 4x5 matrix
matrix = array.reshape(4, 5)

# Print the matrix
print("4x5 Matrix:")
print(matrix)

# Print statistics
print("\nSum of all elements:", matrix.sum())
print("Mean:", matrix.mean())
print("Standard Deviation:", matrix.std())

# Find maximum value in each row
print("\nMaximum value in each row:")
print(matrix.max(axis=1))'''









# Q.10)
import numpy as np

try:
    
    n = int(input("Enter how many numbers you want to generate: "))

    if n <= 0:
        print("Please enter a positive number.")

    else:
        arr = np.random.randint(10, 101, n)

        print("\nArray:")
        print(arr)

        #Print statistics
        print("\nStatistics")
        print("Mean:", arr.mean())
        print("Median:", np.median(arr))
        print("Standard Deviation:", arr.std())
        print("Minimum Value:", arr.min())
        print("Maximum Value:", arr.max())

        #reshape into a 2D array
        if n % 2 == 0:
            matrix = arr.reshape(2, n // 2)

            print("\n2D Array:")
            print(matrix)

            # Print row-wise sum
            print("\nRow-wise Sum:")
            print(matrix.sum(axis=1))
        else:
            print("\nCannot reshape into a 2D array because the number of elements is odd.")

except ValueError:
    print("Invalid input! Please enter an integer.")