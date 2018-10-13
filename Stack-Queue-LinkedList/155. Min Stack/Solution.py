class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.__stack = []
        self.__min = None

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if len(self.__stack) == 0:
            self.__min = [x]
        else:
            self.__min.append(min(self.__min[-1],x))

        self.__stack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        self.__min.pop()
        return self.__stack.pop()

    def top(self):
        """
        :rtype: int
        """
        topValue = self.__stack.pop()

        self.__stack.append(topValue)
        return topValue

    def getMin(self):
        """
        :rtype: int
        """
        return self.__min[-1]
        
# --------------- Follow Up ------------------------
# this is follow up: optimize the space useage of stack 2 if there are a lot of duplicate elements in stack1
# like 2222221111112134333333311111-1
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.__stack = []
        self.__min = None

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if len(self.__stack) == 0:
            self.__min = [{x:1}]
        else:
            for key,value in self.__min[-1].items():
                if x == value:
                    self.__min[-1][key] += 1
                else:
                    self.__min.append({min(x, key):1})

        self.__stack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        if len(self.__stack) == 0:
            return None
        for key in self.__min[-1]:
            if self.__min[-1][key] == 1:
                self.__min.pop()
            else:
                self.__min[-1][key] -= 1

        return self.__stack.pop()

    def top(self):
        """
        :rtype: int
        """
        topValue = self.__stack.pop()

        self.__stack.append(topValue)
        return topValue

    def getMin(self):
        """
        :rtype: int
        """
        for key in self.__min[-1]:
            return key

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
