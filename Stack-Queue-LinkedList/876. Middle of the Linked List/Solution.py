# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# return second node if there are two mid (even length)
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head or not head.next:
            return head

        slow = node
        fast = node
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

# return 1st node if there are two mid (even length)
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head or not head.next:
            return head

        slow = node
        fast = node
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow