class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        res_str = ''
        if len(word1) >= len(word2):
            for index, char in enumerate(word2):
                res_str += word1[index]
                res_str += word2[index]
            word1 = word1[len(word2):]
            res_str += word1
        else:
            for index, char in enumerate(word1):
                res_str += word1[index]
                res_str += word2[index]
            word2 = word2[len(word1):]
            res_str += word2
        return res_str
        

# 双指针
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        res_str = ''
        
        i = 0
        j = 0
        while i + j < len(word1) + len(word2):
            if i < len(word1):
                res_str += word1[i]
                i += 1
            if j < len(word2):
                res_str += word2[j]
                j += 1
        
        return res_str

        
            

