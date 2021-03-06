class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.inQueue = []
        self.outQueue = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.outQueue.append(x)
        while self.inQueue:
            self.outQueue.append(self.inQueue.pop(0))
        self.inQueue,self.outQueue = self.outQueue,self.inQueue


    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.inQueue.pop(0)


    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.inQueue[0]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return not self.inQueue

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()