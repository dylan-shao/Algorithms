# stack1 [4,5,6, 7, 8]
# stack2 [3,2]

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []
        self.front = None

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        if len(self.stack1) == 0:
            self.front = x
        self.stack1.append(x)


    # Amortized O(1) as for n element, first time call pop: n(pop from stack1) + n(push into stack2) + 1(pop) = 2n+1
    # 2 - n times call pop: 1
    # so we have 2n + 1 + 1*(n-1) = 3n, 3n/n -->O(1)
    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if len(self.stack2) == 0:
            while len(self.stack1):
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if len(self.stack2):
            top = self.stack2.pop()
            self.stack2.append(top)
            return top

        return self.front

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.stack1) == 0 and len(self.stack2) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
