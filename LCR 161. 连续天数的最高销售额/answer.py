class Solution(object):
    def maxSales(self, sales):
        """
        :type sales: List[int]
        :rtype: int
        """
        dp = [0] * len(sales)
        dp[0] = sales[0]
        for i in range(1, len(sales)):
            if dp[i - 1] <= 0:
                dp[i] = sales[i]
            else:
                dp[i] = sales[i] + dp[i - 1]
        return max(dp)


