class Solution:
    def sort(self, list):
        low = 0
        high = len(list) - 1
        Solution.helper(list, low, high)
        return list
    def helper(list, low, high):
        if low < high:
            pivot = Solution.partition(list, low, high)
            Solution.helper(list, low, pivot - 1)
            Solution.helper(list, pivot, high)
    def partition(list, low, high):
        pivot = list[high]
        high -= 1
        while low <= high:
            while list[low] < pivot:
                low += 1
            while list[high] > pivot:
                high -= 1
            if low <= high:
                list[low], list[high] = list[high], list[low]
                low += 1
                high -= 1
        return low
