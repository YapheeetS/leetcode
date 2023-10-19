# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 对于每一个非叶子节点，我们只需要分别计算其左右子树的最小叶子节点深度。这样就将一个大问题转化为了小问题，可以递归地解决该问题。
        if root == None:
            return 0
        elif root.left == None and root.right == None:
            return 1
        elif root.left != None and root.right == None:
            left_depth = self.minDepth(root.left)
            return left_depth + 1
        elif root.left == None and root.right != None:
            right_depth = self.minDepth(root.right)
            return right_depth + 1
        else:
            left_depth = self.minDepth(root.left)
            right_depth = self.minDepth(root.right)
            return min(left_depth, right_depth) + 1
        
        



        