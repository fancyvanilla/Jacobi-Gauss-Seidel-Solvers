import numpy as np
import time
from GaussSeidel import GS
from Jacobi import Jacobi
import matplotlib.pyplot as plt


def test_method(method, matrix_sizes):
    avg_times = []

    for size in matrix_sizes:
        runtimes = []
        b = np.random.rand(size)
        matrix = np.random.rand(size, size)

        for _ in range(5): 
            start_time = time.time()

            method(matrix, size, b)

            end_time = time.time()

            runtime = end_time - start_time
            runtimes.append(runtime)

        avg_times.append(np.mean(runtimes))

    return avg_times

def main():
    matrix_sizes=[100, 400, 500, 700, 1000, 1500 ,2000]

    avg_times_Jacobi = test_method(Jacobi, matrix_sizes)
    avg_times_GS = test_method(GS, matrix_sizes)

    smoothed_y1 = np.convolve(avg_times_Jacobi, np.ones(3), mode='same') / 3
    smoothed_y2 = np.convolve(avg_times_GS, np.ones(3), mode='same') / 3

    plt.plot(matrix_sizes, smoothed_y1, label='Jacobi')
    plt.plot(matrix_sizes, smoothed_y2, label='Gauss-Seidel')
    plt.legend() 
    plt.xlabel("Taille de la matrice")
    plt.ylabel("Temps d'exécution (secondes)")
    plt.title("Comparaison des temps d'exécution entre Jacobi et Gauss-Seidel")
    plt.show("figure1")


if __name__ == "__main__":
    main()
