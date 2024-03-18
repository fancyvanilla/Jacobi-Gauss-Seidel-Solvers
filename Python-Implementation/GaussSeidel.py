import numpy as np

def generate_diagonally_dominant(matrix,size):
    for i in range(size):
        row_sum = np.sum(np.abs(matrix[i, :])) - np.abs(matrix[i, i]) 
        matrix[i, i] += row_sum * 1.1  
    return matrix


def GS(matrix, n, b, tolerance=1e-8, omega=1):
    matrix=generate_diagonally_dominant(matrix,n) #ensures that the matrix will converge
    sol = np.zeros(n)
    it = 0
    while True:
        it += 1
        prev = sol.copy()
        for j in range(n):
            sum = 0
            for k in range(n):
                if k != j:
                    sum += sol[k] * matrix[j, k]
            sol[j] = omega*(b[j] - sum) / matrix[j, j] + (1-omega)*sol[j]
        if np.allclose(sol, prev, atol=tolerance, rtol=0):
            print(f"Solution converged in {it} iterations.")
            break
    return sol

#added here error messages
def GS2(matrix, n, b, tolerance=1e-8,omega=1):
    matrix=generate_diagonally_dominant(matrix,n)
    sol = np.zeros(n)
    it = 0
    try:
        while True:
            it += 1
            prev = sol.copy()
            for j in range(n):
                if matrix[j, j] == 0:
                    pass
                sum = 0
                for k in range(n):
                    if k != j:
                        sum += sol[k] * matrix[j, k]
                if abs(b[j]) > 1e10 or abs(sum) > 1e10:
                    raise OverflowError("Potential overflow detected!")
                sol[j] = omega*(b[j] - sum) / matrix[j, j] + (1-omega)*sol[j]
            if np.allclose(sol, prev, atol=tolerance, rtol=0):
                print(f"Solution converged in {it} iterations.")
                break
    except Exception as e:
        print(f"Error occurred: {e}")
        print(f"Iterations completed: {it}")



size = 1000
matrix = np.random.rand(size, size)

b = np.random.rand(size)

GS(matrix, size, b)