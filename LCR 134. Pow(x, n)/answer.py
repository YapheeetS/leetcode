class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        def recur(x, n):
            if n == 0: return 1
            y = recur(x, n // 2)
            if n % 2 == 0:
                return y * y
            else:
                return y * y * x
        
        if n >= 0:
            return recur(x, n)
        else:
            return 1.0 / recur(x, -n)