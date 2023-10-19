class MyLinkedList(object):

    def __init__(self):

        self.val = []


    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index > len(self.val) -1:
            return -1
        return self.val[index]


    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.val.insert(0, val)


    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.val.append(val)


    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index == len(self.val):
            self.val.append(val)
        elif index > len(self.val):
            return
        else:
            self.val.insert(index, val)


    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index > len(self.val) -1:
            return None
        self.val.pop(index)



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)