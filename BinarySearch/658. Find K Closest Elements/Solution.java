import java.util.*; 
class Solution {
    public List<Integer> findClosestElements(int[] arr, int k, int x) {
        List<Integer> res = new ArrayList<Integer>();
        if(arr.length<=1) {
            res.add(arr[0]);
            return res;
        }
        int i = 0;
        int j = arr.length - 1;
        
        while(i<j-1) {
            int mid = i + (j-i)/2;
            if(arr[mid] <= x){
                i = mid;
            }else {
                j = mid;
            }
        }
        j = i+1;
        while(k>0) {
			// check j and i first, in case out of index exception
            if(j>arr.length-1||i>=0 && Math.abs(arr[i]-x)<= Math.abs(arr[j]-x)){
                res.add(arr[i]);
               i--;
            }else {
                res.add(arr[j]);
                j++;
            }
            k--;
        }
        Collections.sort(res);
        return res;
    }
}
