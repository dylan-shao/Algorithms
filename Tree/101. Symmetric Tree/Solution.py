# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        return self.__helper(root.left, root.right)
        
    def __helper(self, node1, node2):
        if node1 == None and node2 == None:
            return True
        elif node1 == None or node2 == None:
            return False
        elif node1.val != node2.val:
            return False
        
        return self.__helper(node1.left, node2.right) and self.__helper(node1.right, node2.left)
        
        