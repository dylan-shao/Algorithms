class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] result = new int[n];
        result[0] = 1;

        for(int i=1;i<n;i++) {
          result[i] = result[i-1]*nums[i-1];
        }

        int prod = 1;

        for(int j=n-1;j>=0;j--) {
          result[j] =  prod*result[j];
          prod = prod * nums[j];
        }

        return result;
    }
}
