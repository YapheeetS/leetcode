class Solution(object):
    def spiralArray(self, array):
        """
        :type array: List[List[int]]
        :rtype: List[int]
        """
        # 将矩阵第一行的元素添加到 res 列表里，删除第一行（也就是 matrix 中的第一个列表），然后逆时针旋转（这里通过转置+倒序实现），新的 matrix 的第一行即为接下来要打印的元素。
        res = []
        while matrix:
            res += matrix.pop(0)
            matrix = list(zip(*matrix))[::-1]
        return res
        