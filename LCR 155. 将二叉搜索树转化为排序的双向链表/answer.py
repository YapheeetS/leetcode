"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        def dfs(node):
            if not node: return
            dfs(node.left)
            if not self.pre: # 第一个节点
                self.head = node
            else:
                node.left = self.pre
                self.pre.right = node
            self.pre = node
            dfs(node.right)

        if not root: return None
        self.pre = None
        dfs(root)
        self.head.left = self.pre
        self.pre.right = self.head
        return self.head