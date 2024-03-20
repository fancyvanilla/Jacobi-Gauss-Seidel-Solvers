import java.util.Arrays;
import java.util.Random;


public class LinearSystemSolver {
@FunctionalInterface
public interface Solver {
    double[] solve(double[][] A, double[] b, int maxIterations, double tolerance);
}

public static double[][] generateRandomMatrix(int n) {
    Random rand = new Random();
    double[][] matrix = new double[n][n];

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            matrix[i][j] = rand.nextDouble();
        }
        double rowSum = 0.0;
        for (int j = 0; j < n; j++) {
            if (i != j) {
                rowSum += Math.abs(matrix[i][j]);
            }
        }
        matrix[i][i] = rowSum*(rand.nextDouble()+1); 
    }
    return matrix;
}

public static double[] generateRandomVector(int n) {
    Random rand = new Random();
    double[] vector = new double[n];

    for (int i = 0; i < n; i++) {
        vector[i] = rand.nextDouble();
    }
    return vector;
}

public static double[] test_method(Solver solver) {
    int [] matrix_sizes={100, 400, 500, 700, 1000, 1500 ,2000};
    double[][] A;
    double[] b;
    double[] runTimes;
    double[] avgTimes=new double[7];
    int maxIterations = 1000;
    double tolerance = 1e-6;
    double[] solution;

    for (int i= 0; i <7 ; i++) {
        A = generateRandomMatrix(matrix_sizes[i]);
        b = generateRandomVector(matrix_sizes[i]);
        runTimes = new double[5];

        for (int j = 0; j < 5; j++) {
            long startTime = System.nanoTime();

            solution = solver.solve(A, b, maxIterations, tolerance);
            
            long endTime = System.nanoTime();
            runTimes[j] = (endTime - startTime) / 1e6;  // Convert to milliseconds
        }
        avgTimes[i] = Arrays.stream(runTimes).average().orElse(0.0);
    }
    return avgTimes;
}

    public static void main(String[] args) {
       double[] avgTimesJacobi= test_method(jacobi::jacobiSolver);; //testing Jacobi
       double[] avgTimesGaussSeidel =test_method(gaussSeidel::gaussSeidelSolver); // testing gauss seidel
    }
}
