# Given the root to a binary tree, implement serialize(root),
# which serializes the tree into a string, and deserialize(s),
# which deserializes the string back into the tree.
#
# For example, given the following Node class
#
# class TreeNode:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# The following test should pass:
#
# node = Node('root', Node('left', Node('left.left')), Node('right'))
# assert deserialize(serialize(node)).left.left.val == 'left.left'
# Google


class Solution:
    def serialize(self, node):
        s = ''
        if node is None:
            s += 'null,'
        else:
            s += str(node.val) + ','

            left = self.serialize(node.left)
            s += left

            right = self.serialize(node.right)
            s += right

        return s




    def deserialize(self, string):
        def helper(l):
            if l[0] == 'null':
                l.pop(0)
                return None
            node = TreeNode(int(l.pop(0)))
            node.left = helper(l)
            node.right = helper(l)

            return node

        list = string.split(',')
        return helper(list)
