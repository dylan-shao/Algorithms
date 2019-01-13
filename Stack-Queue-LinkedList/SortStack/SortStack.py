# sort stack using two additional stacks
import sys

class Solution:
  def __init__(self):
    self.stack1 = []
    self.stack2 = []

  def sort(self, stack):
    while len(stack) > 0 or len(self.stack1) > 0:
      global_min = sys.maxsize
      while len(stack) > 0:
        tmp = stack.pop()
        global_min = min(global_min, tmp)
        self.stack1.append(tmp)
      
      while len(self.stack1) > 0:
        tmp = self.stack1.pop()
        if tmp == global_min:
          self.stack2.append(tmp)
        else:
          stack.append(tmp)
    return self.stack2
      
      
instance = Solution()

sorted_stack = instance.sort([3,4,5,2,1,2,4,5,6,7,8,8])
print(sorted_stack)