# time complexity: 
# O(n),  because transver every node once

class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

class Solution:
  def get_height(self, node):
    if node == None:
      return 0
    
    return 1 + max(self.get_height(node.left), self.get_height(node.right))


sut = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(2)
root.left.right = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(3)
root.right.right = TreeNode(3)
print(sut.get_height(root) == 3)

root.right.right.left = TreeNode(3)
root.right.right.left.right = TreeNode(3)
print(sut.get_height(root) == 5)
