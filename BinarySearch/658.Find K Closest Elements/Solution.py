class Solution:
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        if len(arr) == 0 or k == 0:
            return []

        left = 0
        right = len(arr) - 1
        # start = -1
        res = []
        while left < right - 1:
            mid = left + (right - left) // 2

            if arr[mid] == x:
                left = mid
                right = mid
                break
            elif arr[mid] < x:
                left = mid
            else:
                right = mid
        # left, right will be either equal (found x), or nighbor(not found x)
        # not found, nighbor, find which is close to x, take it as start
        if left != right:
            if x - arr[left] > arr[right] - x:
                res.append(arr[right])
                left = right
            else:
                res.append(arr[left])
                right = left
        else:
            res.append(arr[left])


        while k > 1:
            if left >= 0:
                left -= 1
            if right <= len(arr) - 1:
                right += 1

            if left < 0:
                res.append(arr[right])
            elif right > len(arr) - 1:
                res = [arr[left]] + res
            elif x - arr[left] <= arr[right] - x:
                res = [arr[left]] + res
                right -= 1
            else:
                res.append(arr[right])
                left += 1
            k -= 1

        return res

# original answer
# class Solution:
#     def findClosestElements(self, arr, k, x):
#         """
#         :type arr: List[int]
#         :type k: int
#         :type x: int
#         :rtype: List[int]
#         """
#         if len(arr) == 0 or k == 0:
#             return []
#
#         left = 0
#         right = len(arr) - 1
#         start = -1
#         res = []
#         while left < right - 1:
#             mid = left + (right - left) // 2
#
#             if arr[mid] == x:
#                 start = mid
#                 break
#             elif arr[mid] < x:
#                 left = mid
#             else:
#                 right = mid
#
#         # not found, or in left or right
#         if start == -1:
#             #edge case
#             if arr[left] > x:
#                 return arr[:k]
#             if arr[right] < x:
#                 return arr[-k:]
#             if x - arr[left] > arr[right] - x:
#                 start = right
#             else:
#                 start = left
#         left = start
#         right = start
#         res.append(arr[start])
#
#         while k > 1:
#             if left >= 0:
#                 left -= 1
#             if right <= len(arr) - 1:
#                 right += 1
#
#             if left < 0:
#                 res.append(arr[right])
#             elif right > len(arr) - 1:
#                 res = [arr[left]] + res
#
#             elif x - arr[left] <= arr[right] - x:
#                 res = [arr[left]] + res
#                 right -= 1
#             else:
#                 res.append(arr[right])
#                 left += 1
#             k -= 1
#         return res
#
