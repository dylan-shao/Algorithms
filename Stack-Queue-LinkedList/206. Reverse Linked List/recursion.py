# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        new_head =  self.reverseList(head.next)

        head.next.next  = head
        head.next = None
        
        return new_head
# class Solution:
#     def reverseList(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
#         if head == None or head.next == None:
#             return head
        
#         new_head = self.__helper(head)
#         head.next = None
#         return new_head
    
#     def __helper(self, node):
#         if node.next == None:
#             return node
#         new_head = self.__helper(node.next)
#         node.next.next = node
#         return new_head