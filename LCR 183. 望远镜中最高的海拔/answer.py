class Solution(object):
    def maxAltitude(self, heights, limit):
        """
        :type heights: List[int]
        :type limit: int
        :rtype: List[int]
        """
        if heights == []:
            return []
        res = []
        length = len(heights) - limit
        for i in range(length+1):
            res.append(max(heights[i:i+limit]))
        return res
