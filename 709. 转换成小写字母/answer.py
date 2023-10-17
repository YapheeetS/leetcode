class Solution(object):
    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        """
        # return s.lower()
    
        #自行实现API
        # (1) 可以通过哈希表实现（A, a）, (B, b)
        # (2) ASCII 码, 大写字母 A-Z [65, 90]，小写字母a-z [97, 122]
        res = ""
        for i, ch in enumerate(s):
            if 65 <= ord(ch) <= 90:
                res += chr(ord(ch) + 32)
            else:
                res += ch
        return res