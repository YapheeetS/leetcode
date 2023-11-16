class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.A, self.B = [], []


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.A.append(x)
        if len(self.B) == 0 or x <= self.B[-1]:
            self.B.append(x)

    def pop(self):
        """
        :rtype: None
        """
        num = self.A.pop()
        if num == self.B[-1]:
            self.B.pop()


    def top(self):
        """
        :rtype: int
        """
        return self.A[-1]


    def getMin(self):
        """
        :rtype: int
        """
        return self.B[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()