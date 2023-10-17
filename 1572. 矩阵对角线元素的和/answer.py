class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        sum1 = sum2 = 0
        for i in range(len(mat)):
            sum1 += mat[i][i]
            sum2 += mat[i][len(mat)-i-1]
        sum_all = sum1 + sum2
        if len(mat) % 2 != 0:
            sum_all -= mat[len(mat)/2][len(mat)/2]

        return sum_all