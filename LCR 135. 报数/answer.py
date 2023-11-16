# 简单方法
class Solution(object):
    def countNumbers(self, cnt):
        """
        :type cnt: int
        :rtype: List[int]
        """
        max_num = 10 ** cnt
        res = []
        for i in range(1, max_num):
            res.append(i)
        return res


# 大数打印
class Solution(object):
    def countNumbers(self, cnt):
        """
        :type cnt: int
        :rtype: List[int]
        """
        def dfs(x):
            if x == cnt:
                str_num =  ''.join(num).lstrip('0')
                if str_num != '':
                    res.append(int(str_num))
                return
            for i in range(10):
                num[x] = str(i)
                dfs(x + 1)
        res = []
        num = ['0'] * cnt
        dfs(0)
        return res