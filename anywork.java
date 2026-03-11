import java.util.*;

public class CoffeeTemperature {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int MAX_TEMP = 200001;

        int n = sc.nextInt();
        int k = sc.nextInt();
        int q = sc.nextInt();

        int[] diff = new int[MAX_TEMP + 1];

        
        for (int i = 0; i < n; i++) {
            int l = sc.nextInt();
            int r = sc.nextInt();
            diff[l] += 1;
            if (r + 1 < MAX_TEMP) {
                diff[r + 1] -= 1;
            }
        }

        
        int[] count = new int[MAX_TEMP + 1];
        for (int i = 1; i < MAX_TEMP; i++) {
            count[i] = count[i - 1] + diff[i];
        }

       
        int[] admissible = new int[MAX_TEMP + 1];
        for (int i = 1; i < MAX_TEMP; i++) {
            admissible[i] = (count[i] >= k) ? 1 : 0;
        }

       
        int[] prefixAdmissible = new int[MAX_TEMP + 1];
        for (int i = 1; i < MAX_TEMP; i++) {
            prefixAdmissible[i] = prefixAdmissible[i - 1] + admissible[i];
        }

        
        StringBuilder output = new StringBuilder();
        for (int i = 0; i < q; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            int result = prefixAdmissible[b] - prefixAdmissible[a - 1];
            output.append(result).append("\n");
        }

        System.out.print(output.toString());
        sc.close();
    }
}