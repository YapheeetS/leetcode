class Solution(object):
    def bestTiming(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # dp[i]: 前i日卖出的最大利润
        # dp[i] = max(dp[i−1], prices[i] − min(prices[0:i]))
        min_price = float("inf")
        res = 0
        for price in prices:
            min_price = min(min_price, price)
            res = max(res, price - min_price)
        return res

