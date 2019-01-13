# complexity O(1), Amortized O(1)
class Deque:
  def __init__(self):
    self.stack1 = []
    self.stack2 = []
    self.stack3 = []

  def l_append(self, n):
    self.stack1.append(n)

  def r_append(self, n):
    self.stack2.append(n)

  def l_pop(self):
    if len(self.stack1) == 0 and len(self.stack2) != 0:
      self.__balance_left()
      
    if len(self.stack1):
      return self.stack1.pop()
    else:
      if len(self.stack2) == 1:
        return self.stack2.pop()
      else:
        return None

  def r_pop(self):
    if len(self.stack2) == 0 and len(self.stack1) != 0:
      self.__balance_right()

    if len(self.stack2):
      return self.stack2.pop()
    else:
      if len(self.stack1) == 1:
        return self.stack1.pop()
      else:
        return None

  def l_peek(self):
    if len(self.stack1) == 0:
      self.__balance_left()

    value = self.stack1.pop()
    self.stack1.append(value)
    return value

  def r_peek(self):
    if len(self.stack2) == 0:
      self.__balance_right()
    
    value = self.stack2.pop()
    self.stack2.append(value)
    return value

  def is_empty(self):
    return len(self.stack1) == 0 and len(self.stack2) == 0

  def __balance_left(self):
    n = len(self.stack2)

    while len(self.stack2):
      if len(self.stack2)  > n/2:
        self.stack3.append(self.stack2.pop())
      else:
        self.stack1.append(self.stack2.pop())

    while len(self.stack3):
      self.stack2.append(self.stack3.pop())

  def __balance_right(self):
    n = len(self.stack1)

    while len(self.stack1):
      if len(self.stack1) > n/2:
        self.stack3.append(self.stack1.pop())
      else:
        self.stack2.append(self.stack1.pop())
    while len(self.stack3):
      self.stack1.append(self.stack3.pop())


d = Deque()

d.r_append(5)
d.r_append(6)
d.r_append(7)
d.r_append(8)
d.l_append(4)
d.l_append(3)
d.l_append(2)
d.l_append(1)

while not d.is_empty():
  print('should print 1 to 8 ', str(d.l_pop()) + " ")

d.l_append(4)
d.l_append(3)
d.l_append(2)
d.l_append(1)


print('should right pop 4: ', d.r_pop())