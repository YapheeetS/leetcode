class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        # prices[i] - min(prices[0:i])
        min_price = float('+inf')
        res = 0
        for price in prices:
            min_price = min(price, min_price)
            res = max(price - min_price, res)
        return res
