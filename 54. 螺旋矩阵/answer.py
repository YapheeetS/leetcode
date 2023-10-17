class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        """
        j++
        i++
        j--
        i--
        
        """
        # 列表展开
        all_num = sum(matrix, [])
        res = []
        len_j = len(matrix[0])
        len_i = len(matrix)
        ben_j = 0
        ben_i = 1
        i = j = 0
        # print(all_num)
        # 0, 1, 2, 3记录方向右、下、左上
        direct = 0
        while(len(all_num) > 0):
            # print(i,j)
            # print(matrix[i][j])
            res.append(matrix[i][j])
            all_num.remove(matrix[i][j])
            # print(all_num)
            if direct == 0: # j++
                if j < len_j - 1:
                    j += 1
                else: # 变换方向，且减少len_j
                    i += 1
                    len_j -= 1
                    direct = 1
            elif direct == 1: # i++
                if i < len_i - 1:
                    i += 1
                else: # 变换方向，且减少len_i
                    j -= 1
                    len_i -= 1
                    direct = 2
            elif direct == 2: # j--
                if j > ben_j:
                    j -= 1
                else: # 变换方向，且增加ben_j
                    i -= 1
                    ben_j += 1
                    direct = 3
            else: # i--
                if i > ben_i:
                    i -= 1
                else:
                    j += 1
                    ben_i += 1
                    direct = 0
        
        return res

