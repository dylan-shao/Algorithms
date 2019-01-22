# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
  def insert(self, head, node):
    origin_head = head
    if node.val < head.val:
      node.next = head
      return node
    while head.next:
      if node.val <= node.val and node.val <= head.next.val:
        node.next = head.next
        head.next = node
        return origin_head
      else:
        head = head.next
    head.next = node
    node.next = None
    return origin_head



def print_helper(head, msg, target=None):
  count = 1
  print('--------start-----------')
  print(msg)
  while head:
    if count and head.val == target:
      print('\'{}\''.format(head.val))
      count -= 1
    else:
      print(head.val)
    head = head.next
  print('--------end-----------')

def get_a():
  a = ListNode(2)
  b = ListNode(2)
  c = ListNode(4)
  d = ListNode(5)

  a.next = b
  b.next = c
  c.next = d

  return a

a = get_a()
print_helper(a, 'test a')

sut = Solution()

r = sut.insert(get_a(), ListNode(2))
print_helper(r, 'insert 2 in a', 2)

r = sut.insert(get_a(), ListNode(3))
print_helper(r, 'insert 3 in a', 3)

r = sut.insert(get_a(), ListNode(4))
print_helper(r, 'insert 4 in a', 4)

r = sut.insert(get_a(), ListNode(5))
print_helper(r, 'insert 5 in a', 5)

r = sut.insert(get_a(), ListNode(6))
print_helper(r, 'insert 6 in a', 6)