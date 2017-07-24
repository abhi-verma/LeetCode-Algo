class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []
        self.stack = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.queue.insert(0, x)
        
    def queueToStack(self):
        """
        Shifts the elements from the queue to stack
        """
        while self.queue:
            self.stack.append(self.queue.pop())

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        self.queueToStack()
        if len(self.stack) > 0:
          return self.stack.pop()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        self.queueToStack()
        if len(self.stack) > 0:
          return self.stack[-1]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.stack) == 0 and len(self.queue) == 0


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
obj.push(2)
print(obj.top())
obj.push(3)
print(obj.top())
