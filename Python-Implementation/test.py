import numpy as np
import time
import matplotlib.pyplot as plt
from GaussSeidel import GS
from Jacobi import Jacobi


matrix_sizes=[100, 400, 500, 700, 1000, 1500 ,2000]
avg_times_Jacobi=[]
avg_times_GS=[]

for size in matrix_sizes:
    runtimes1 = []
    runtimes2 = []
    b = np.ones(size)
    matrix = np.random.rand(size, size)


    for _ in range(5): 
        #Jacobi
        start_time = time.time()

        Jacobi(matrix,size,b)

        end_time = time.time()

        runtime = end_time - start_time
        runtimes1.append(runtime)
        #Seidel
        start_time = time.time()

        GS(matrix,size,b)

        end_time = time.time()

        runtime = end_time - start_time
        runtimes2.append(runtime)


    avg_runtime = sum(runtimes1) / 5
    avg_times_Jacobi.append(avg_runtime)

    avg_runtime = sum(runtimes2) / 5
    avg_times_GS.append(avg_runtime)


x = matrix_sizes
y1 = avg_times_Jacobi
y2 = avg_times_GS



smoothed_y1 = np.convolve(y1, np.ones(3), mode='same') / 3
smoothed_y2 = np.convolve(y2, np.ones(3), mode='same') / 3


plt.plot(x, smoothed_y1, label="Données lissées Jacobi")
plt.plot(x, smoothed_y2, label="Données lissées Gauss-Seidel")

plt.legend()
plt.xlabel("Taille de la matrice")
plt.ylabel("Temps d'exécution (secondes)")

plt.show()