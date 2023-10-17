from itertools import permutations
class Solution(object):
    def tictactoe(self, moves):
        """
        :type moves: List[List[int]]
        :rtype: str
        """
        
        A = moves[::2] # 步长为2取一次数据
        B = moves[1::2] # 起始index为1步长为2取一次数据
        print(A)
        """
        (c[1]-b[1])/(c[0]-b[0]) = (b[1]-a[1])/(b[0]-a[0])
        """
        for a,b,c in itertools.permutations(A, 3):
            if (c[1] - b[1])*(b[0] - a[0]) == (b[1] - a[1])*(c[0] - b[0]):
                return "A"
        for a,b,c in itertools.permutations(B, 3):
            if (c[1] - b[1])*(b[0] - a[0]) == (b[1] - a[1])*(c[0] - b[0]):
                return "B"
        
        if len(A) + len(B) == 9:
            return "Draw"
        else:
            return "Pending"
