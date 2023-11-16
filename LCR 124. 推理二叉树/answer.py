# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# “无重复节点值” 的二叉树
class Solution(object):
    def deduceTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        def recur(root, left, right):
            if left > right: return
            # 根据先序遍历数组，建立根节点
            node = TreeNode(preorder[root])
            #  查找根节点在中序遍历 inorder 中的索引 i
            i = hmap[preorder[root]]
            """
            node.left参数解释
            # root + 1: 左子树在先序数组中根结点的索引
            # left: 左子树在中序数组中的左边界
            # i-1: 左子树在中序数组中的右边界
            """
            node.left = recur(root + 1, left, i - 1)
            """
            node.right参数解释
            # root + i - left + 1: 右子树在先序数组中根结点的索引 （根节点索引 + 左子树长度 + 1）
            # i + 1: 右子树在中序数组中的左边界
            # right: 左子树在中序数组中的右边界
            """
            node.right = recur(root + i - left + 1, i + 1, right)
            return node

        # 记录中序遍历 inorder 中各个节点的索引
        hmap = {}
        for i in range(len(inorder)):
            hmap[inorder[i]] = i
        return recur(0, 0, len(inorder) - 1)



