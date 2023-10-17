# 方法2：把指令直接循环4次看是否在0
class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        """
        "G"：直走 1 个单位
        "L"：左转 90 度
        "R"：右转 90 度
        """
        # 当前方向0北,1东,2南,3西
        direction = [0,1,2,3]
        # 当前坐标
        x = y = 0
        instructions = instructions + instructions + instructions + instructions
        for ins in instructions:
            if ins == 'G' and direction[0] == 0:
                y += 1
            elif ins == 'G' and direction[0] == 1:
                x += 1
            elif ins == 'G' and direction[0] == 2:
                y -= 1
            elif ins == 'G' and direction[0] == 3:
                x -= 1
            elif ins == 'L':
                direction = direction[-1:] + direction[:-1]
            elif ins == 'R':
                direction = direction[1:] + direction[:1]
        if x == 0 and y == 0:
            return True
        else:
            return False




class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        """
        "G"：直走 1 个单位
        "L"：左转 90 度
        "R"：右转 90 度
        """
        # 方法1：机器人想要摆脱循环，在一串指令之后的状态，必须是不位于原点且方向朝北。
        direction = [0,1,2,3]
        # 当前坐标
        x = y = 0
        for ins in instructions:
            if ins == 'G' and direction[0] == 0:
                y += 1
            elif ins == 'G' and direction[0] == 1:
                x += 1
            elif ins == 'G' and direction[0] == 2:
                y -= 1
            elif ins == 'G' and direction[0] == 3:
                x -= 1
            elif ins == 'L':
                direction = direction[-1:] + direction[:-1]
            elif ins == 'R':
                direction = direction[1:] + direction[:1]
        
        if x == 0 and y == 0:
            return True
        else:
            if direction[0] == 0:
                return False
            else:
                return True