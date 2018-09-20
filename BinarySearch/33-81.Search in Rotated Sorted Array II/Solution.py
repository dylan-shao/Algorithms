# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
#
# (i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).
#
# You are given a target value to search. If found in the array return true, otherwise return false.
#
# Example 1:
#
# Input: nums = [2,5,6,0,0,1,2], target = 0
# Output: true
# Example 2:
#
# Input: nums = [2,5,6,0,0,1,2], target = 3
# Output: false

class Solution:
    def search(self, nums, target):
        if len(nums) == 0:
            return False

        left = 0
        right = len(nums) - 1

        while(left < right -1 ):
            mid = (left + right) // 2


            if nums[mid] == target:
                return True

            if nums[mid] > nums[left]:
                #(r1, r1, left) (r1, r1,right) (r1,r2,left)
                # see detailed comments on 33. python solution
                if nums[mid] > target and target >= nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] < nums[right]:
                # (r2, r2, right) (r2, r2, left) (r2,r1,right)
                if nums[mid] < target and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if nums[left] == target:
                    return True
                else:
                    left += 1

                if nums[right] == target:
                    return True
                else:
                    right -= 1

        if nums[left] == target:
            return True
        elif nums[right] == target:
            return True
        else:
            return False
