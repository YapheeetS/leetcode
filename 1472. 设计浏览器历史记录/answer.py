class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.pointer = 0
        self.url_list = [homepage]


    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        self.url_list = self.url_list[:self.pointer+1]
        # if url in 
        self.url_list.append(url) 
        self.pointer += 1


    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        if self.pointer - steps >= 0:
            self.pointer -= steps
        else:
            self.pointer = 0
        return self.url_list[self.pointer]



    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        if self.pointer + steps < len(self.url_list) - 1:
            self.pointer += steps
        else:
            self.pointer = len(self.url_list) - 1
        return self.url_list[self.pointer]





# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)