class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        map = {}
        for idx, val in enumerate(numbers):
            if val in map:
                return [map[val], idx]

            if not target - val in map:
                map[target - val] = idx
