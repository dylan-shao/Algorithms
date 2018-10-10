# O(log(max(m,n)))
# suppose m > n
# O(log(m) + log(n)) < O(2*log(m)) = O(log(m))

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        if m == 0:
            return False

        n = len(matrix[0])

        if n == 0:
            return False

        left = 0
        right = m - 1
        row = -1

        # find the row
        while left < right - 1:
            mid = left + (right - left) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target and matrix[mid - 1][0] < target:
                row = mid - 1
                break
            elif matrix[mid][0] > target:
                right = mid
            else:
                left = mid
        # if not found row, check left and right
        print(left, right, row)
        if row == -1:
            # boundary
            if matrix[left][0] > target and left == 0:
                return False
            if matrix[right][n-1] < target and right == m - 1:
                return False
            # check either left row or right row
            if matrix[left][0] <= target and matrix[right][0] > target:
                row = left
            if matrix[right][0] <= target and matrix[right][n-1] >= target:
                row = right

        # binary search target in row
        left = 0
        right = n - 1
        while left <= right:
            mid = left + (right - left) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False

# class Solution:
#     def searchMatrix(self, matrix, target):
#         """
#         :type matrix: List[List[int]]
#         :type target: int
#         :rtype: bool
#         """
#         m = len(matrix)
#         if m == 0:
#             return False
#
#         n = len(matrix[0])
#
#         if n == 0:
#             return False
#
#         left = 0
#         right = m - 1
#         row = -1
#
#         # find the row
#         while left < right:
#             mid = left + (right - left) // 2
#             if matrix[mid][0] <= target and matrix[mid][n-1] >= target:
#                 row = mid
#                 break
#             elif matrix[mid][0] > target:
#                 right = mid - 1
#             else:
#                 left = mid + 1
#
#         # if not found row, check left and right
#         if row == -1:
#             # boundary
#             if matrix[left][0] > target and left == 0:
#                 return False
#             if matrix[left][n-1] < target and left == m -1:
#                 return False
#             # check either left row or right row
#             if matrix[left][0] <= target and matrix[left][n-1] >= target:
#                 row = left
#
#         # binary search target in row
#         left = 0
#         right = n - 1
#         while left <= right:
#             mid = left + (right - left) // 2
#             if matrix[row][mid] == target:
#                 return True
#             elif matrix[row][mid] < target:
#                 left = mid + 1
#             else:
#                 right = mid - 1
#
#         return False
