import java.util.*;

public class WordDifferences {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String first = scanner.nextLine();
        String second = scanner.nextLine();

        int operations = editDistDP(first, second);

        System.out.printf("Deletions and Insertions: %d%n", operations);
    }

    private static int editDistDP(String first, String second) {
        int[][] dp = new int[first.length() + 1][second.length() + 1];
        int m = first.length(), n = second.length();
        for (int i = 0; i <= m; i++) {
            for (int j = 0; j <= n; j++) {
                if (i == 0) {
                    dp[i][j] = j;
                } else if (j == 0) {
                    dp[i][j] = i;
                } else if (first.charAt(i - 1) == second.charAt(j - 1)) {
                    dp[i][j] = dp[i - 1][j - 1];
                } else {
                    dp[i][j] = 1 + Math.min(dp[i][j - 1], dp[i - 1][j]);
                }
            }
        }

        return dp[m][n];
    }
}
