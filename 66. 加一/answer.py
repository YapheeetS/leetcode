# 先转整数，再转数组
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        number = 0
        for i, num in enumerate(digits):
            number += digits[i] * (10**(len(digits) - i - 1))
        number = number + 1
        print(number)

        #判断是否多了一位
        if number / 10**(len(digits)) == 0:
            num_list = [0]*len(digits)
        else:
            num_list = [0]*(len(digits) + 1)
        
        for i in range(len(num_list)):
            n = number / (10**(len(num_list) - i - 1))
            # print(n)
            number -= n*10**(len(num_list) - i - 1)
            # print(number)
            num_list[i] = n
        return num_list


# python黑科技
# 利用map进行数组int类型与str类型的转换
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        d = str(int("".join(map(str, digits))) + 1)
        return map(int, list(d))