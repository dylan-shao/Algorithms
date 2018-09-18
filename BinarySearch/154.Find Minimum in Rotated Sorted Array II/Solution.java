class Solution {
    public int findMin(int[] nums) {
        if(nums.length == 0) {
            return -1;
        }
        
        int left = 0;
        int right = nums.length - 1;
        while(left < right - 1) {
            int mid = left + (right-left)/2;
            if(nums[mid]<nums[right] ){
                right = mid;
            }else if(nums[mid]>nums[right]){
                left = mid;
            }else { // == right
                if(nums[mid] == nums[left]){
                    left++;
                }
                right--;
            }
        }
        return  Math.min(nums[left],nums[right]);
        
    }
}
