# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        list1 = ListNode(0)
        list2 = ListNode(0)
        head1 = list1
        head2 = list2
        
        while head:
            if head.val < x:
                list1.next = head
                list1 = list1.next
                head = head.next
            else:
                list2.next = head
                list2 = list2.next
                head = head.next
                
        list1.next = head2.next
        list2.next = None
        
        return head1.next

