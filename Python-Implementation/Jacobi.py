import numpy as np
from GaussSeidel import generate_diagonally_dominant


def Jacobi(matrix, n, b, tolerance=1e-8, omega=1):
    matrix=generate_diagonally_dominant(matrix,n)
    sol = np.zeros(n)
    it = 0
    try:
        while True:
            it += 1
            curr = []
            for j in range(n):
                if matrix[j, j] == 0:
                    pass
                sum = 0
                for k in range(n):
                    if k != j:
                        sum += sol[k] * matrix[j, k]
                if abs(b[j]) > 1e10 or abs(sum) > 1e10:
                    raise OverflowError("Potential overflow detected!")
                curr.append(omega*(b[j] - sum) / matrix[j, j] + (1-omega)*sol[j])
            if np.allclose(sol, curr, atol=tolerance, rtol=0):
                print(f"Solution converged in {it} iterations.")
                break
            sol=curr
            curr=[]
    except Exception as e:
        print(f"Error occurred: {e}")
        print(f"Iterations completed: {it}")
