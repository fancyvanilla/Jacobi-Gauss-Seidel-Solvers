import java.util.Arrays;

public class LinearSystemSolver {

    // Méthode pour résoudre un système linéaire avec l'algorithme de Jacobi
    public static double[] jacobi(double[][] A, double[] b, int maxIterations, double tolerance) {
        int n = A.length;
        double[] x = new double[n];
        double[] xNew = new double[n];
        Arrays.fill(x, 0); // Initialisation du vecteur x

        for (int k = 0; k < maxIterations; k++) {
            for (int i = 0; i < n; i++) {
                double sum = b[i];
                for (int j = 0; j < n; j++) {
                    if (i != j) {
                        sum -= A[i][j] * x[j];
                    }
                }
                xNew[i] = sum / A[i][i];
            }

            // Vérification de la convergence
            double maxDiff = 0;
            for (int i = 0; i < n; i++) {
                double diff = Math.abs(xNew[i] - x[i]);
                if (diff > maxDiff) {
                    maxDiff = diff;
                }
            }
            if (maxDiff < tolerance) {
                return xNew; // La solution a convergé
            }

            // Mise à jour de x
            System.arraycopy(xNew, 0, x, 0, n);
        }

        return null; // La solution n'a pas convergé dans le nombre maximal d'itérations
    }

    // Méthode pour résoudre un système linéaire avec l'algorithme de Gauss-Seidel
    public static double[] gaussSeidel(double[][] A, double[] b, int maxIterations, double tolerance) {
        int n = A.length;
        double[] x = new double[n];
        Arrays.fill(x, 0); // Initialisation du vecteur x

        for (int k = 0; k < maxIterations; k++) {
            double maxDiff = 0;
            for (int i = 0; i < n; i++) {
                double sum = b[i];
                double diag = A[i][i];
                for (int j = 0; j < n; j++) {
                    if (i != j) {
                        sum -= A[i][j] * x[j];
                    }
                }
                double xNew = sum / diag;

                // Vérification de la convergence partielle
                double diff = Math.abs(xNew - x[i]);
                if (diff > maxDiff) {
                    maxDiff = diff;
                }

                x[i] = xNew;
            }

            if (maxDiff < tolerance) {
                return x; // La solution a convergé
            }
        }

        return null; // La solution n'a pas convergé dans le nombre maximal d'itérations
    }

    public static void main(String[] args) {
        // Exemple d'utilisation
        double[][] A = { { 4, -1, 0 }, { -1, 4, -1 }, { 0, -1, 3 } };
        double[] b = { 12, -1, 0 };
        int maxIterations = 1000;
        double tolerance = 1e-6;

        double[] solutionJacobi = jacobi(A, b, maxIterations, tolerance);
        double[] solutionGaussSeidel = gaussSeidel(A, b, maxIterations, tolerance);

        System.out.println("Solution avec Jacobi: " + Arrays.toString(solutionJacobi));
        System.out.println("Solution avec Gauss-Seidel: " + Arrays.toString(solutionGaussSeidel));
    }
}
