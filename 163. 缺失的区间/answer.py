class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[List[int]]
        """

        result = []
        if len(nums) == 0:
            return [[lower, upper]]
        
        pointer = 0
        for index, num in enumerate(nums):
            if index == 0:
                if lower + 1 <= num:
                    result.append([lower, num - 1])
                    lower = num
                else:
                    lower = num
            else:

                if lower + 1 < num:
                    result.append([lower + 1, num - 1])
                    lower = num
                else:
                    lower = num
        
        if lower < upper:
            result.append([lower + 1, upper])

        return result