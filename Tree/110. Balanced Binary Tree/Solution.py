# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        return self.__helper(root) != -1
        
    def __helper(self, root):
        if root == None:
            return 0
    
        left_height = self.__helper(root.left)
        right_height = self.__helper(root.right)
        
        if left_height == -1 or right_height == -1:
            return -1
        
        left_height += 1
        right_height += 1
        
        if abs(left_height - right_height) <= 1:
            return max(left_height, right_height)
        else:
            return -1
        