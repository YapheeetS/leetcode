class Solution(object):
    def statisticalResult(self, arrayA):
        """
        :type arrayA: List[int]
        :rtype: List[int]
        """
        res = []
        mul_num = 1
        if 0 in arrayA:
            for num in arrayA:
                if num != 0:
                    mul_num *= num
                    res.append(0)
                else:
                    res.append(-1)

            zero_count = res.count(-1)
            if zero_count > 1:
                return [0] * len(arrayA)
            else:
                index = res.index(-1)
                res[index] = mul_num
            return res

        res = []
        mul_num = 1
        for num in arrayA:
            mul_num *= num
        
        for num in arrayA:
            res.append(mul_num/num)
        
        return res