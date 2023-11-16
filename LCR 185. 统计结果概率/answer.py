class Solution(object):
    def statisticsProbability(self, num):
        """
        :type num: int
        :rtype: List[float]
        """
        dp = [1.0 / 6] * 6 # num-1的概率数组
        for i in range(2, num + 1):
            temp = [0] * (5 * i + 1)
            for j in range(len(dp)):
                for k in range(6):
                    temp[j + k] += dp[j] / 6
            dp = temp
        return dp


import torch
import torch.nn.functional as F
class Solution:
    def dicesProbability(self, n):
        # 初始化单个骰子的概率分布
        # tensor([[[0.1667, 0.1667, 0.1667, 0.1667, 0.1667, 0.1667]]])
        single_dice_prob = torch.tensor([1.0 / 6] * 6).view(1, 1, 6)
        print(single_dice_prob)
        # 初始情况，只有一个骰子
        # tensor([[[0.1667, 0.1667, 0.1667, 0.1667, 0.1667, 0.1667]]])
        n_dice_prob = torch.tensor([1.0 / 6] * 6).view(1, 1, 6) 
        for _ in range(n - 1):
            # 更新概率分布
            n_dice_prob = F.conv1d(n_dice_prob, single_dice_prob, padding=5).view(1, 1, -1)
            print(n_dice_prob)
        return n_dice_prob.squeeze()
    

# solution = Solution()
# res = solution.dicesProbability(3)
# print(res)