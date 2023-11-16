# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathTarget(self, root, target):
        """
        :type root: Optional[TreeNode]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        path = []
        def dfs(root, target):
            if not root: return
            path.append(root.val)
            target -= root.val
            if target == 0 and not root.left and not root.right:
                res.append(list(path))
            dfs(root.left, target)
            dfs(root.right, target)
            path.pop()

        dfs(root, target)
        return res



"""
以 Python 语言为例，记录路径时若直接执行 res.append(path) ，则是将此 path 对象加入了 res ；后续 path 改变时，res 中的 path 对象也会随之改变，因此无法实现结果记录。正确做法为：

"""