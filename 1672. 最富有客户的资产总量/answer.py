class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        max_acc = 0
        for acc in accounts:
            sum_acc = sum(acc)
            if sum_acc > max_acc:
                max_acc = sum_acc
        return max_acc