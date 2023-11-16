class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0: return 1
        if n == 1: return 1
        a, b = 1, 1
        for i in range(1, n):
            a, b = b, a + b
        return b