class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        i = 0
        j = 0  # 记录前两个数的位置
        res = []
        for ops in operations:
            if ops == 'C':
                res.pop()
            elif ops == 'D':
                res.append(res[-1] * 2)
            elif ops == '+':
                res.append(res[-1] + res[-2])
            else:
                ops = int(ops)
                res.append(ops)
        return sum(res)


