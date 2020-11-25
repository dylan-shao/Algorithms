package SelectionSort;

import java.util.Arrays;

public class SS2 {
    private void selectionSort(int[] l) {
        if (l.length <= 1) {
            return;
        }

        for (int i = 0;i < l.length - 1; i++) {
            int globalMinIndex = i;
            for (int j = i + 1; j < l.length; j ++) {
                if (l[j] < l[globalMinIndex]) {
                    globalMinIndex = j;
                }
            }
            if (globalMinIndex != i) {
                this.swap(l, i , globalMinIndex);
            }
        }
    }

    private void swap(int[] l, int i, int j) {
        int temp = l[i];
        l[i] = l[j];
        l[j] = temp;
    }
    public static void main(String[] args) {
        SS2 t = new SS2();
        int[] l = new int[]{19,6,5,3,1,3,5,3,6,4,3,2,3,3,5,99,102};
        t.selectionSort(l);
        System.out.println(Arrays.toString(l));
    }
}
