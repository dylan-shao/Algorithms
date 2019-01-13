# sort stack using only one additional stack
import sys

class Solution:
  def __init__(self):
    self.stack1 = []

  def sort(self, stack):
    init_length = 0

    while len(stack):
      count = 0
      globla_min = sys.maxsize
      while len(stack):
        tmp = stack.pop()
        globla_min = min(globla_min, tmp)
        self.stack1.append(tmp)
      while len(self.stack1) > init_length:
        tmp = self.stack1.pop()
        if tmp == globla_min:
          count += 1
        else:
          stack.append(tmp)
      while count:
        self.stack1.append(globla_min)
        count -= 1
        
      init_length = len(self.stack1)

    return self.stack1

instance = Solution()
stack = [3,4,5,2,1,2,4,5,6,7,8,8,1]
print(stack)
sorted_stack = instance.sort(stack)
print(sorted_stack)