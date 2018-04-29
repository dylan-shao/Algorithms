class Solution {
    public int[] searchRange(int[] nums, int target) {
        int[] res = new int[]{-1,-1};
        if(nums.length==0 || nums[0]>target || nums[nums.length-1]<target) {
            return res;
        }
        
        res[0] = getFirstOccurance(nums, target);
        res[1] = getLastOccurance(nums, target);
        
        return res;
        
    }
    
    public int getFirstOccurance(int[] nums,int target) {
        int left = 0;
        int right = nums.length - 1;
        while(left < right -1) {
            int mid = left + (right-left)/2;
           if( nums[mid]<target) {
                left = mid;
            } else {
                right = mid;
            }
        }
        if(nums[left] == target) {
            return left;
        }
        if(nums[right] == target) {
            return right;
        }
        return -1;
    }
    
     public int getLastOccurance(int[] nums,int target) {
        int left = 0;
        int right = nums.length - 1;
        while(left < right -1) {
            int mid = left + (right-left)/2;
           if( nums[mid]>target) {
                right = mid;
            } else {
                left = mid;
            }
        }
        if(nums[right] == target) {
            return right;
        }
        if(nums[left] == target) {
            return left;
        }
        return -1;
    }
}
