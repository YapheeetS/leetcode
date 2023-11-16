class Solution(object):
    def verifyTreeOrder(self, postorder):
        """
        :type postorder: List[int]
        :rtype: bool
        """
        def recur(i, j):
            if i >= j: return True
            m = i
            while(postorder[m] < postorder[j]):
                m += 1
            n = m
            while(postorder[n] > postorder[j]):
                n += 1
            if n == j:
                return recur(i, m-1) and recur(m, j-1)
            else:
                return False
        return recur(0, len(postorder) - 1)



        