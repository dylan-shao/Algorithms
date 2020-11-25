package BubbleSort;

import java.util.Arrays;

public class BubbleSort {
    public int[] bubbleSort(int[] array) {
        boolean switched = true;
        while (switched == true ) {
            switched = false;
            for (int i =0; i< array.length - 1;i++) {
                int j = i + 1;
                if (array[j] < array[i]) {
                    switched = true;
                    swap(array, i, j);
                }
            }
        }
//        do {
//            for (int i =0; i< array.length - 1;i++) {
//                int j = i + 1;
//                if (array[j] < array[i]) {
//                    switched = true;
//                    swap(array, i, j);
//                }
//            }
//        } while (switched == false );
        return array;
    }

    public static void swap(int[] arr, int i, int j) {
        int tmp = arr[i];
        arr[i] = arr[j];
        arr[j] = tmp;
    }

    public static void main(String[] args)
    {
        int[] a = new int[]{3,4,3,1,56,7,3,2,1,5,11,2,33};
        BubbleSort instance = new BubbleSort();
        instance.bubbleSort(a);
        System.out.print(Arrays.toString(a));
    }
}
