class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s_list = []
        for cha in s:
            s_list.append(cha)
        for cha in t:
            if cha not in s_list:
                return cha
            else:
                s_list.remove(cha)
                

# 记录每个字符的出现次数，python中可以利用 Counter
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        return ((Counter(t) - Counter(s)).keys()[0])
    

# 把两个字符串加起来，使用异或的方法找到只出现一次的字符

"""
按位与（&）,按位或（|）,按位异或（^),按位取反（~） 
按位异或（^):相同位为0，否则为1。异或具有交换律，结合律，自反性，因此最后剩的就是多的字符
"""

class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        r = s + t
        result = 0
        for cha in r:
            result = result ^ ord(cha)
        return chr(result)