class Solution {
    public int search(int[] nums, int target) {
        if(nums.length == 0 || nums == null || target <nums[0]&& target > nums[nums.length-1]) {
            return -1;
        }
        
        int left = 0;
        int right = nums.length -1;
        
        while(left<=right){
            int mid = left + (right - left)/2;
            if(nums[mid] == target) {
                return mid;
            }
            
            if(nums[mid]>=nums[left] ){  // two range, this is for mid is in the first range
                if(nums[mid]>target && target >= nums[left]) {
                    right= mid-1;
                }else  {
                    left = mid+1;
                }
            }else { //  this is for mid is in the second range
                if(nums[mid]<target && target<=nums[right]) {
                    left = mid+1;
                }else {
                    right = mid-1;
                }
            }
        }
        
        return -1;
    }
}


// class Solution {
//     public int search(int[] nums, int target) {
//         if(nums.length == 0 || nums == null || target <nums[0]&& target > nums[nums.length-1]) {
//             return -1;
//         }
        
//         int left = 0;
//         int right = nums.length -1;
        
//         while(left<=right){
//             int mid = left + (right - left)/2;
//             if(nums[mid] == target) {
//                 return mid;
//             }else if(nums[mid]>=nums[0] ){  // two range, this is for mid is in the first range
//                 if(nums[mid]>target && target >= nums[0]) {
//                     right= mid-1;
//                 }else  {
//                     left = mid+1;
//                 }
//             }else { //  this is for mid is in the second range
//                 if(nums[mid]<target && target<=nums[nums.length - 1]) {
//                     left = mid+1;
//                 }else {
//                     right = mid-1;
//                 }
//             }
//         }
        
//         return -1;
//     }
// }
