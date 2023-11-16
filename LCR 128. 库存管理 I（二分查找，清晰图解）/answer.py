# 暴力搜索
class Solution(object):
    def stockManagement(self, stock):
        """
        :type stock: List[int]
        :rtype: int
        """
        if len(stock) == 1:
            return stock[0]
        for i in range(1, len(stock)):
            if stock[i] < stock[i-1]:
                return stock[i]
        return stock[0]

