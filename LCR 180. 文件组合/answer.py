class Solution(object):
    def fileCombination(self, target):
        """
        :type target: int
        :rtype: List[List[int]]
        """
        i = j = 1
        sum_num = 0
        res = []
        while i <= target // 2:
            if sum_num < target:
                sum_num += j
                j += 1
            elif sum_num > target:
                sum_num -= i
                i += 1
            else:
                arr = list(range(i,j))
                res.append(arr)
                sum_num -= i
                i += 1
        return res
            


