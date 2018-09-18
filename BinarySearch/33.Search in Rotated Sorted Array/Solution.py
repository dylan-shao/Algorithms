# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
#
# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
#
# You are given a target value to search. If found in the array return its index, otherwise return -1.
#
# You may assume no duplicate exists in the array.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# Example 1:
#
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:
#
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) <= 0:
            return -1
        left = 0
        right = len(nums) - 1

        while left < right - 1:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                if nums[middle] > nums[left]:
                    left = middle + 1
                else:
                    if nums[right] >= target:
                        left = middle + 1
                    else:
                        right = middle - 1
            else:
                if nums[middle] > nums[left]:
                    if nums[left] <= target:
                        right = middle - 1
                    else:
                        left = middle + 1
                else:
                    right = middle - 1


        if nums[left] == target:
            return left
        elif nums[right] == target:
            return right
        else:
            return -1
