class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        arr.sort()
        num = arr[1] - arr[0]
        for i in range(len(arr) - 1):
            if arr[i+1] - arr[i] != num:
                return False
        return True
