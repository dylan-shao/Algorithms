class Solution {
    public int searchInsert(int[] nums, int target) {
        if(nums.length==0 || nums==null) {
            return -1;
        }
        
        int left = 0;
        int right = nums.length -1 ;
        while(left < right -1) {
            int mid = left + (right-left) /2 ;
            if(nums[mid] <= target) {
                left = mid;
            }else {
                right = mid;
            }
        }
        
        if(nums[left] >= target) {
            return left;
        }else if(nums[right]>=target){
            return right;
        }
        return right + 1;
    }
}
