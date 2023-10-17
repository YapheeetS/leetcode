# 利用flag记录是否需要减
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # I,V,X,L,C,D,M
        # IV,IX,XL,XC,CD,CM

        num_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        s_l = list(s)
        n_l = [num_dict[ch] for ch in s_l]
        flag = False
        res = 0
        for index, num in enumerate(n_l):
            # print(res)
            if flag:
                flag = False
                res = res + num - n_l[index - 1]
                continue
            if index < len(n_l) - 1:
                if num < n_l[index + 1]: #
                    flag = True
                    continue
                else:
                    res += num
            else:
                res += num
        
        return res

# 黑科技
"""
构建一个字典记录所有罗马数字子串，注意长度为 2 的子串记录的值是（实际值 - 子串内左边罗马数字代表的数值）
这样一来，遍历整个 s 的时候判断当前位置和前一个位置的两个字符组成的字符串是否在字典内，如果在就记录值，不在就说明当前位置不存在小数字在前面的情况，直接记录当前位置字符对应值
get(key, default) 函数可以通过 key 从 d 中找出对应的值，如果 key 不存在则返回默认值 default
"""
class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I':1, 'IV':3, 'V':5, 'IX':8, 'X':10, 'XL':30, 'L':50, 'XC':80, 'C':100, 'CD':300, 'D':500, 'CM':800, 'M':1000}
        return sum(d.get(s[max(i-1, 0):i+1], d[n]) for i, n in enumerate(s))
