class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        num_five = 0
        num_ten = 0

        for b in bills:
            if b == 5:
                num_five += 1
            elif b == 10:
                if num_five > 0:
                    num_five -= 1
                    num_ten += 1
                else:
                    return False
            elif b == 20:
                if num_ten > 0:
                    if num_five > 0:
                        num_five -= 1
                        num_ten -= 1
                    else:
                        return False
                else:
                    if num_five > 2:
                        num_five -= 3
                    else:
                        return False
        
        return True

