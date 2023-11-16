class Solution(object):
    def __init__(self):
        self.res = 0

    def mechanicalAccumulator(self, target):
        """
        :type target: int
        :rtype: int
        """
        # 逻辑运算符的短路效应
        target > 1 and self.mechanicalAccumulator(target - 1)
        self.res += target
        return self.res

