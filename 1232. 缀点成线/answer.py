class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        for i in range(len(coordinates) - 2):
            if (coordinates[i+1][1] - coordinates[i][1]) * (coordinates[i+2][0] - coordinates[i][0])  != (coordinates[i+2][1] - coordinates[i][1]) * (coordinates[i+1][0] - coordinates[i][0]):
                return False
        return True
