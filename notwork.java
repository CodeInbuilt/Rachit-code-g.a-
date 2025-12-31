class Work {
    void merge(int a[], int start, int mid, int end) {
        int p = start, q = mid + 1, k = 0;
        int[] arr = new int[end - start + 1];
        
        while (p <= mid && q <= end) {
            if (a[p] < a[q]) {
                arr[k++] = a[p++];
            } else {
                arr[k++] = a[q++];
            }
        }
        
        while (p <= mid) {
            arr[k++] = a[p++];
        }
        
        while (q <= end) {
            arr[k++] = a[q++];
        }
        
        for (int i = 0; i < k; i++) {
            a[start++] = arr[i];
        }
    }
    
    void merge_sort(int a[], int start, int end) {
        if (start < end) {
            int mid = (start + end) / 2;
            merge_sort(a, start, mid);
            merge_sort(a, mid + 1, end);
            merge(a, start, mid, end);
        }
    }
}
