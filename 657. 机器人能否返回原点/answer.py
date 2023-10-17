class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        move_dict = Counter(moves)
        return move_dict['U'] == move_dict['D'] and move_dict['R'] == move_dict['L']
        