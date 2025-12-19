import java.util.Arrays;
import java.util.Scanner;

public class KthElement {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {

            
            System.out.print("Enter size of array: ");
            int n = sc.nextInt();
            int[] arr = new int[n];

            System.out.println("Enter elements of array:");
            for (int i = 0; i < n; i++) {
                arr[i] = sc.nextInt();
            }

           
            System.out.print("Enter value of k: ");
            int k = sc.nextInt();

            
            Arrays.sort(arr);

            
            int kthSmallest = arr[k - 1];
           
            int kthLargest = arr[n - k];

            System.out.println(k + "th Smallest element: " + kthSmallest);
            System.out.println(k + "th Largest element: " + kthLargest);
        }
    }
}
