class Solution(object):
    def buddyStrings(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """

        if len(s) != len(goal):
            return False
        if s == goal: # 字符串完全相同
            if len(set(s)) < len(goal): #有重复的字符
                return True
            else:
                return False
        diff = [(a, b) for a, b in zip(s, goal) if a != b]
        if len(diff) != 2:
            return False
        if diff[0][0] == diff[1][1] and diff[0][1] == diff[1][0]:
            return True
        else:
            return False