# 暴力
class Solution(object):
    def findTargetIn2DPlants(self, plants, target):
        """
        :type plants: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for li in plants:
            if target in li:
                return True
        return False
    
# 分治
class Solution(object):
    def findTargetIn2DPlants(self, plants, target):
        """
        :type plants: List[List[int]]
        :type target: int
        :rtype: bool
        """
        i = len(plants) - 1
        j = 0
        while i >= 0 and j <= len(plants[0]) - 1:
            if plants[i][j] > target:
                i -= 1
            elif plants[i][j] < target:
                j += 1
            else:
                return True
        return False