public class moveZeroesToEnd {
    public static void moveZeroesToEnd(int[] arr) {
        int index = 0; // Position to place the next non-zero element
        for (int num : arr) {
            if (num != 0) {
                arr[index++] = num;
            }
        }
        // Fill the rest of the array with zeroes
        while (index < arr.length) {
            arr[index++] = 0;
        }
    }

    public static void main(String[] args) {
        int[] arr = {0, 1, 0, 3, 12};
        moveZeroesToEnd(arr);
        for (int num : arr) {
            System.out.print(num + " ");
        }
    }
}