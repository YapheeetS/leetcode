# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def checkSymmetricTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def recur(L, R):
            if not L and not R: return True
            if not L or not R or L.val != R.val: return False
            return recur(L.left, R.right) and recur(L.right, R.left)

        if not root:
            return True
        
        return recur(root.left, root.right)
        
