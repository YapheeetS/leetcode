# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 递归
class Solution(object):

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        out = []
        def dfs(root):
            if root == None:
                return
            
            left = dfs(root.left)
            out.append(root.val)
            right = dfs(root.right)
        
        dfs(root)
        return out
    
# 非递归,利用栈
class Solution(object):

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        stack = []
        while len(stack) > 0 or root != None:
            if root:
                stack.append(root)
                root = root.left
            else:
                curr = stack.pop()
                result.append(curr.val)
                root = curr.right
        return result
        

# 莫里斯遍历（没有使用任何辅助空间）
class Solution(object):

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        res = []
        pre = None
        while root: 
            # 如果左节点不为空，就将当前节点连带右子树全部挂到左节点的最右子树下面
            if root.left:
                pre = root.left
                # 寻找最右子树
                while pre.right:
                    pre = pre.right
                # 此时 pre 是左节点的最右子树
                pre.right = root
                # 将root设置为root.left，并且原本的root.left需要置为None
                temp = root
                root = root.left
                temp.left = None
            else:
                res.append(root.val)
                root = root.right
        return res