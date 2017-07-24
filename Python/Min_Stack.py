class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = None
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if not self.stack:
          self.stack.append(0)
          self.min = x
        else:
          self.stack.append(x-self.min)
          if x < self.min:
            self.min = x

    def pop(self):
        """
        :rtype: void
        """
        x = self.stack.pop()
        if x < 0:
          self.min = self.min - x
    
    def top(self):
        """
        :rtype: int
        """
        if self.stack:
          x = self.stack[-1]
          if x < 0:
            return self.min
          else:
            return x + self.min

    def getMin(self):
        """
        :rtype: int
        """
        return self.min
        


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(5)
obj.push(6)
obj.push(7)
obj.pop()
print(obj.top())
print(obj.getMin())
