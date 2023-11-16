class Solution(object):
    def dismantlingAction(self, arr):
        """
        :type arr: str
        :rtype: str
        """
        counter_dict = Counter(arr)
        for c in arr:
            if c in counter_dict and counter_dict[c] == 1:
                return c
        return ' '


