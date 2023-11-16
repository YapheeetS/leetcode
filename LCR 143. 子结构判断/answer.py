# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# BFS
class Solution(object):
    def isSubStructure(self, A, B):
        """
        :type A: TreeNode
        :type B: TreeNode
        :rtype: bool
        """
        # 判断A、B节点及其子节点是否都相同
        def helper(A, B):
            queue = [(A, B)]
            while queue:
                nodeA, nodeB = queue.pop(0)
                if not nodeA or nodeA.val != nodeB.val:
                    return False
                if nodeB.left:
                    queue.append((nodeA.left, nodeB.left))
                if nodeB.right:
                    queue.append((nodeA.right, nodeB.right))
            return True


        if not B:
            return False
        deque = collections.deque()
        deque.append(A)
        while deque:
            node = deque.popleft()
            if node.val == B.val:
                if helper(node, B):
                    return True
            if node.left: deque.append(node.left)
            if node.right: deque.append(node.right)
        return False
                


# DFS
class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def recur(A, B):
            if not B: return True
            if not A or A.val != B.val: return False
            return recur(A.left, B.left) and recur(A.right, B.right)

        return bool(A and B) and (recur(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B))

