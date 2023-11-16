class Solution(object):
    def trainWays(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0: return 1
        if num == 1: return 1
        a, b = 0, 1
        for i in range(0, num):
            a, b = b, a + b
        return b % 1000000007
