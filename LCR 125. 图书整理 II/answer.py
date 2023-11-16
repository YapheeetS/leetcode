class CQueue(object):

    def __init__(self):
        self.q_list = []


    def appendTail(self, value):
        """
        :type value: int
        :rtype: None
        """
        return self.q_list.append(value)


    def deleteHead(self):
        """
        :rtype: int
        """
        if len(self.q_list) > 0:
            q = self.q_list[0]
            self.q_list = self.q_list[1:]
            return q
        else:
            return -1



# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()