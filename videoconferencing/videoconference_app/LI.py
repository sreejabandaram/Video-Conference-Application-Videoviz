import numpy as np

def is_linearly_independent(vectors):
    # Convert the list of vectors into a NumPy array
    matrix = np.array(vectors)
    
    # Use Gaussian elimination to reduce the matrix to row echelon form
    _, _ = matrix.shape
    for i in range(len(matrix)):
        pivot = matrix[i, i]
        if pivot == 0:
            return False  # If a zero pivot is encountered, vectors are linearly dependent
        matrix[i] /= pivot
        for j in range(i + 1, len(matrix)):
            factor = matrix[j, i]
            matrix[j] -= factor * matrix[i]
    
    return True

# Example usage:
vectors = [
    [1, 1, 1],
    [-1, 2, -3],
    [0, -3, 2]
]

result = is_linearly_independent(vectors)

if result:
    print("The set of vectors is linearly independent.")
else:
    print("The set of vectors is linearly dependent.")
