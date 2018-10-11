# O(n) worst case
class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return None

        left = 0
        right = n - 1

        while left < right - 1:
            mid = left + (right - left) // 2
            # range 1
            if nums[mid] > nums[n-1]:
                left = mid
            # range 2
            elif nums[mid] < nums[n-1]:
                right = mid
            # edge case,
            else:
                left = mid
                right = mid
                while left > 0:
                    left -= 1

                    if nums[left] >= nums[n-1] and nums[left+1] < nums[n-1]:
                        return nums[left + 1]

                while right < n - 1:
                    right += 1

                    if nums[right] < nums[n-1] and nums[right-1] >= nums[n-1]:
                        return nums[right]
                break

        return nums[left] if nums[left] <= nums[right] else nums[right]
