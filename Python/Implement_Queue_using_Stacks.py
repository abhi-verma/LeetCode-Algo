class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        self.queue = []
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
    
    def stackToQueue(self):
        """
        Removes the element from the top of the stack and appends them to the queue
        """
        if len(self.queue) == 0:
          while self.stack:
            self.queue.append(self.stack.pop())

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        self.stackToQueue()
        if len(self.queue) > 0:
          return self.queue.pop()
        

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        self.stackToQueue()
        if len(self.queue) > 0:
          return self.queue[-1]
        

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.stack) == 0 and len(self.queue) == 0

# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(5)
obj.push(4)
obj.push(3)
param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()

print(param_2, param_3, param_4)
