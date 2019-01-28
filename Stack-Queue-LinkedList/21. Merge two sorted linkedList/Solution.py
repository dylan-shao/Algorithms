# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def merge(n1, n2):
  dummy_node = ListNode(0)
  head = dummy_node


  while n1 != None and n2 != None:
    dummy_node.next = ListNode(0)
    dummy_node = dummy_node.next

    if n1.val <= n2.val:
      dummy_node.val = n1.val
      n1 = n1.next
    else:
      dummy_node.val = n2.val
      n2 = n2.next

  if n1 != None:
    dummy_node.next = n1
  else:
    dummy_node.next = n2
  
  return head.next

# solution without extra space needed
class Solution:
    def mergeTwoLists(self, n1, n2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy_node = ListNode(0)
        head = dummy_node


        while n1 != None and n2 != None:
            if n1.val <= n2.val:
              dummy_node.next = n1
              n1 = n1.next
            else:
              dummy_node.next = n2
              n2 = n2.next
            
            dummy_node = dummy_node.next
            
        if n1 != None:
            dummy_node.next = n1
        else:
            dummy_node.next = n2

        return head.next

#---------------- test -------------------

l1 = ListNode(2)
l1a = ListNode(3)
l1b = ListNode(4)
l1c = ListNode(5)
l1d = ListNode(7)

l1.next = l1a
l1a.next = l1b
l1b.next = l1c
l1c.next = l1d

l2 = ListNode(1.2)
l2a = ListNode(2.5)
l2b = ListNode(4.5)
l2c = ListNode(6)

l2.next = l2a
l2a.next = l2b
l2b.next = l2c

res = merge(l1,l2)
while res.next:
  print(res.val)
  res = res.next
