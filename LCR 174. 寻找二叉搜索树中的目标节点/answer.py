# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTargetNode(self, root, cnt):
        """
        :type root: Optional[TreeNode]
        :type cnt: int
        :rtype: int
        """
        def dfs(node):
            if not node: return
            dfs(node.right)
            if self.cnt == 0: return # 提前返回
            self.cnt -= 1
            if self.cnt == 0:
                self.res = node.val
                return
            dfs(node.left)
        self.cnt = cnt
        dfs(root)
        return self.res