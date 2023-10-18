class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == "0" or num2 == "0":
            return "0"
        
        m, n = len(num1), len(num2)
        ans_list = [0] * (m + n)

        # 从最后向前遍历range(start, stop, step)
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                ans_list[i + j + 1] += int(num1[i]) * int(num2[j])
        
        # ans_list进位问题
        for i in range(n + m - 1, 0, -1):
            print(ans_list)
            ans_list[i - 1] += ans_list[i] // 10 # 整除
            ans_list[i] %= 10 # 余数
        
        if ans_list[0] != 0:
            return "".join(str(x) for x in ans_list)
        else:
            return "".join(str(x) for x in ans_list[1:])
        

                
