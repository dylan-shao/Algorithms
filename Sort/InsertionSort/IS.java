package InsertionSort;

import java.util.Arrays;

public class IS {
    private void insertionSort(int[] l) {
        if (l.length <= 1){
            return;
        }
        for (int i = 1; i< l.length;i++) {


            // key value, left is sorted, right is not sorted
            int key = l[i];
            int k = i;
            for (int j=i-1;j>=0;j--) {
                System.out.println(key + "-" + j +"-" +i + Arrays.toString(l));

                if (l[j] <= key){
                    break;
                }

                this.swap(l, k, j);
                k--;
            }
        }

    }

    private void swap(int[] l, int i, int j) {
        int tmp = l[i];
        l[i] = l[j];
        l[j] = tmp;
    }
    public static void main(String[] args) {
        IS i = new IS();

        // worst case, it's O((n^2 - n)/2) = O(n^2), same as selection sort
        int[] l1 = new int[]{8,7,6,5,4,3,2,1};
        i.insertionSort(l1);
        System.out.println(Arrays.toString(l1));

        // but for array that are sorted or almost sorted, the time complexity is O(kn) when each element is at most k places away from its sorted position.
        int[] l2 = new int[]{1,2,3,4,5,6,7,8};
        i.insertionSort(l2);
        System.out.println(Arrays.toString(l2));
    }
}
