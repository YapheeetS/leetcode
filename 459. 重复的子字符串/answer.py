class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 如果您的字符串 S 包含一个重复的子字符串，那么这意味着可以多次 “移位”字符串，并使其与原始字符串匹配。
        # 使用窗口滑动形式实现
        window = len(s)
        s_new = s + s
        s_new = s_new[1:-1]
        print(s_new)
        return s in s_new
