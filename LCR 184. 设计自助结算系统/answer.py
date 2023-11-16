class Checkout(object):

    def __init__(self):
        self.items = []


    def get_max(self):
        """
        :rtype: int
        """
        if self.items:
            return max(self.items)
        else:
            return -1


    def add(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.items.append(value)



    def remove(self):
        """
        :rtype: int
        """
        if self.items:
            return self.items.pop(0)
        else:
            return -1



# Your Checkout object will be instantiated and called as such:
# obj = Checkout()
# param_1 = obj.get_max()
# obj.add(value)
# param_3 = obj.remove()