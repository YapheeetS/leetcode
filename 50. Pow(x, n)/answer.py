class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # 如果使用暴力循环解答会造成 MemoryError
        # 快速幂
        def quickMul(num):
            if num == 0:
                return 1.0
            # num为1时，quickMul会返回 1 * 1 * x
            y = quickMul(num // 2)
            if num % 2 == 0:
                return y * y
            else:
                return y * y * x
        
        if n >= 0:
            return quickMul(n)
        else:
            return 1.0 / quickMul(-n)
            

