class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return None

        left = 0
        right = len(nums) - 1

        while left < right - 1:
            mid = left + (right - left) // 2
            if nums[mid] > nums[len(nums)-1]:
                left = mid
            else:
                right = mid

        return nums[left] if nums[left] <= nums[right] else nums[right]
