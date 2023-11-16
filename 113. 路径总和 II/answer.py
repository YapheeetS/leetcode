# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        res = []
        path = []
        def dfs(root, target):
            if not root: return
            
            target -= root.val
            path.append(root.val)
            if target == 0 and not root.left and not root.right:
                copy_path = list(path)
                res.append(copy_path)
            dfs(root.left, target)
            dfs(root.right, target)
            path.pop()
        
        dfs(root, targetSum)
        return res
        