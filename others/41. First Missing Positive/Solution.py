# Given an array of integers, find the first missing positive
# integer in linear time and constant space. In other words,
# find the lowest positive integer that does not exist in the array.
# The array can contain duplicates and negative numbers as well.
#
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
#
# You can modify the input array in-place.
# Stripe

class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1

        while left <= right:
            while left < len(nums) and nums[left] > 0:
                left += 1
            while right >= 0 and nums[right] <= 0:
                right -= 1

            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]

        # by this time, nums[0:left] are all positive
        positiveList = nums[0:left]

        # if index not out of range, we change it to negative
        for i in positiveList:
            if abs(i) - 1 < len(positiveList) and positiveList[abs(i) -1] > 0:
                positiveList[abs(i) - 1] = -positiveList[abs(i)-1]

        # just iterate array, if found positive, means that is the first positive missing
        for index, el in enumerate(positiveList):
            if el > 0:
                return index + 1
        return len(positiveList) + 1
