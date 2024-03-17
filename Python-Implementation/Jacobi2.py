from numpy import array, zeros, diag, diagflat, dot
import numpy as np

def jacobi(A,n):
    b = np.random.rand(n)
    b=np.ones(n)
    x=np.zeros(n)
    tolerance=1e-8                                                                                                                                                 
    D = diag(A)
    R = A - diagflat(D)
    it=0
    while True:
        it+=1
        prev=x
        x = (b - dot(R,x)) / D
        if np.allclose(x, prev, atol=tolerance, rtol=0):
                print(f"Solution converged in {it} iterations.")
                print(x)
                break

    return x


jacobi(np.random.rand(20,20),20)
