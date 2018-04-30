class Solution {
    public boolean search(int[] nums, int target) {
        if(nums.length == 0) {
            return false;
        }
        
        int left = 0;
        int right = nums.length -1;
        
        while(left <= right) {
            int mid = left + (right-left)/2;
            if(nums[mid] == target) {
                return true;
            }
            
            if(nums[mid] > nums[left]) {  // first half, without first element
                if(nums[mid]>target && target>=nums[left]) {
                    right = mid -1;
                }else {
                    left = mid+1;
                }
            }else if(nums[mid]<nums[right]) { // second half, without last element
                if(nums[mid]<target && target<=nums[right]) {
                    left = mid + 1;
                }else {
                    right = mid -1;
                }
            }else {  // nums[mid] = nums[left] || nums[mid] == nums[right]
                if(nums[left] == target){
                    return true;
                }else {
                    left ++;
                }
                
                if(nums[right] == target) {
                    return true;
                }else {
                    right--;
                }
            }
        }
        return false;
    }
}
