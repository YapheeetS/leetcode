# 暴力解
import copy
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        new_matrix = copy.deepcopy(matrix)
        for i, m in enumerate(matrix):
            for j, n in enumerate(m):
                if n == 0:
                    for p in range(len(matrix[0])):
                        new_matrix[i][p] = 0
                    for k in range(len(matrix)):
                        new_matrix[k][j] = 0
        for i, m in enumerate(matrix):
            for j, n in enumerate(m):
                matrix[i][j] = new_matrix[i][j]


"""
方法一：使用标记数组

思路和算法
我们可以用两个标记数组分别记录每一行和每一列是否有零出现。
具体地，我们首先遍历该数组一次，如果某个元素为 000，那么就将该元素所在的行和列所对应标记数组的位置置为 true\text{true}true。最后我们再次遍历该数组，用标记数组更新原数组即可。

"""
import copy
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        m, n = len(matrix), len(matrix[0])
        row = [False] * m
        column = [False] * n

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row[i] = True
                    column[j] = True

        for i in range(m):
            for j in range(n):
                if row[i] == True or column[j] == True:
                    matrix[i][j] = 0


