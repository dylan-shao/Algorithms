class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1

        while left < right - 1:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid
            else:
                right = mid

        if nums[left] == target:
            return left
        if nums[right] == target:
            return right

        # three range, < left, <mid>, > right
        if nums[left] > target:
            return left
        elif nums[right] < target:
            return right + 1
        else:
            return left + 1
        
