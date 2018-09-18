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
                # one pivot, so we have two range, range1, range2,
                # where the more left value of range1 is less than most right value of range2
                #
                # lets define a tuple (a,b,c) where "a" represents the position of middle, and "b" represents position of target, "c" represents the value we need to change
                # When nums[middle] < target:
                #    there are 3 options to move:
                #       (r1,r1, left) (r2,r2, left) (r2, r1, right), ------ (r1,r2) is not possible because target need large than nums[middle]
                # if middle in range1, we got (r1,r1, left), so we have 1 option to set left = middle + 1
                #  else if middle in range2, we got (r2,r2, left) (r2, r1, right), we could set either left or right dependes on the target
                # So totally, we have 2 options to set left, and one option to set right, so we find the condition to set right first, because it's only one possible:
                # which is (r2, r1, right) when middle in range2, and target is in range1
                if nums[middle] <= nums[right] and nums[right] < target:
                    right = middle - 1
                else:
                    left = middle + 1
            else:
                # When nums[middle] > target:
                # same as above, (r1,r2, left), (r1, r1, right), (r2, r2, right)
                # so we find the unqiue one which is move left (r1,r2, left)
                if nums[middle] >= nums[left] and nums[left] > target:
                    left = middle + 1
                else:
                    right = middle - 1


        if nums[left] == target:
            return left
        elif nums[right] == target:
            return right
        else:
            return -1
