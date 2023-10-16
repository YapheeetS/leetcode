# 通过计算结果
class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        product = 1
        for num in nums:
            product *= num
        if product > 0:
            return 1
        elif product < 0:
            return -1
        else:
            return 0

# 通过记录正负号
class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        res = 1
        for num in nums:
            if num == 0:
                return 0
            if num < 0:
                res = -res
        return res
