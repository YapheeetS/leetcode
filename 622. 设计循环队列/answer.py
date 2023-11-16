class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.que = [-1] * k
        self.pointer = -1


    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        # print(self.pointer)
        # print(self.que[:10])
        if self.pointer < len(self.que) - 1:
            self.pointer += 1
            self.que[self.pointer] = value
            return True
        else:
            return False
        

    def deQueue(self):
        """
        :rtype: bool
        """
        if self.que[0] != -1:
            self.que = self.que[1:]
            self.que += [-1]
            self.pointer -= 1
            return True
        else:
            return False

    def Front(self):
        """
        :rtype: int
        """
        return self.que[0]


    def Rear(self):
        """
        :rtype: int
        """
        return self.que[self.pointer]


    def isEmpty(self):
        """
        :rtype: bool
        """
        if self.pointer < 0:
            return True
        else:
            return False


    def isFull(self):
        """
        :rtype: bool
        """
        if self.pointer == len(self.que) - 1:
            return True
        else:
            return False




# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()