# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def decorateRecord(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []

        res = []
        q_list = []
        q_list.append(root)
        while q_list:
            node = q_list.pop(0)
            res.append(node.val)
            if node.left:
                q_list.append(node.left)
            if node.right:
                q_list.append(node.right)
        return res

        
