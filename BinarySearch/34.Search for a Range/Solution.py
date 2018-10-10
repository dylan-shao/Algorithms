class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        res = [-1,-1]
        if len(nums) == 0:
            return [-1, -1]
        if len(nums) == 1 and nums[0] == target:
            return [0,0]


        res[0] = self.__get_starting_position(nums, target)
        res[1] = self.__get_ending_position(nums, target)
        return res


    def __get_starting_position(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left < right - 1:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid
            else:
                right = mid
        if nums[left] == target:
            return left
        elif nums[right] == target:
            return right
        else:
            return -1
    def __get_ending_position(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left < right - 1:
            mid = left + (right - left) // 2
            if nums[mid] > target:
                right = mid
            else:
                left = mid
        if nums[right] == target:
            return right
        elif nums[left] == target:
            return left
        else:
            return -1
