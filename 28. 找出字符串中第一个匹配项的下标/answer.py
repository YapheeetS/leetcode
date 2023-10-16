class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)


# 手动实现字符串匹配，暴力解
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        # 暴力匹配
        for i in range(len(haystack) - len(needle) + 1):
            if needle == haystack[i:i+len(needle)]:
                return i
        return -1



# KMP字符串匹配(自己实现)
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # KMP
        # 获取前缀表next数组
        if len(needle) == 0:
            return 0
        next_list = self.getNext(needle)
        print(next_list)

        # 进行匹配
        i = j = 0
        flag = False
        while (i < len(haystack) and j < len(needle)):
            
            # print(i,j)
            if (flag == True and j == 0) or needle[j] == haystack[i]:
                if flag == True and j == 0 and needle[j] != haystack[i]:
                    flag = False
                    i += 1
                else:
                    i += 1
                    j += 1
            else:
                if j == 0:
                    j = next_list[j]
                else:
                    j = next_list[j - 1]
                flag = True
        
        if j == len(needle):
            return i - j
        else:
            return -1
    

    def getNext(self, needle):
        next_list = [0]*len(needle)
        i = 1
        j = 0
        while i < len(needle):
            
            if needle[i] == needle[j]:
                next_list[i] = next_list[i-1] + 1
                i += 1
                j += 1
            else:
                if j == 0:
                    i += 1
                    continue
                next_list[i] = next_list[i-1]
                while j >= 0:
                    if needle[i] != needle[j]:
                        print (i, j, needle[i], needle[j])
                        j = next_list[j - 1]
                        if j == 0:
                            # next_list[i] = 0
                            next_list[i] = j
                            break
                    else:
                        print (i, j, needle[i], needle[j])
                        # next_list[i] = next_list[i] + 1
                        next_list[i] = j+1
                        i += 1
                        j += 1
                        break

                if (j == 0) and (needle[i] == needle[j]):
                    next_list[i] = next_list[i] + 1
                    i += 1
                    j += 1
            
        return next_list








        