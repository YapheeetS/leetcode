class Solution(object):
    def trainingPlan(self, actions):
        """
        :type actions: List[int]
        :rtype: List[int]
        """
        return [num for num in actions if num%2 == 1] + [num for num in actions if num%2 == 0]