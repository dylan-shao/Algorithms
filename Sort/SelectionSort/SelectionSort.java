import java.util.Arrays;

public class SelectionSort {
  public int[] selectionSort(int[] array) {
    if(array==null || array.length <= 1) {
      return array;
    }

    for(int i=0;i<array.length;i++) {
      int globalMinIndex = i;
      for(int j=i+1;j<array.length;j++) {
        if(array[j]<array[globalMinIndex]) {
          swap(array, j, globalMinIndex);
        }
      }
    }
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
    SelectionSort instance = new SelectionSort();
   	instance.selectionSort(a);
   	System.out.print(Arrays.toString(a));
  }
}
