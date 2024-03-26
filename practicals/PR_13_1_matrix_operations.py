import numpy as np

def create_matrix():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    print("Enter the elements row-wise:")
    return np.array([[float(input(f"Enter element at position ({i+1}, {j+1}): ")) for j in range(cols)] for i in range(rows)])

print("Enter details for Matrix 1:")
matrix1 = create_matrix()
print("\nEnter details for Matrix 2:")
matrix2 = create_matrix()

print("\nMatrix 1:")
print(matrix1)
print("Matrix 2:")
print(matrix2)
print("Matrix Addition:")
print(matrix1 + matrix2)
print("Matrix Subtraction:")
print(matrix1 - matrix2)
print("Matrix Multiplication:")
print(np.matmul(matrix1, matrix2))
print("Matrix Division:")
print(matrix1 / matrix2)
