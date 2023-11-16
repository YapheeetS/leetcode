# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 迭代
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        if not root:
            return True
        deque = collections.deque()
        deque.append(root)
        while deque:
            temp = collections.deque()
            for _ in range(len(deque)):
                node= deque.popleft()
                temp.append(node)
                if node: 
                    deque.append(node.left)
                    deque.append(node.right)
            if len(temp) == 1: continue
            for _ in range(len(temp) // 2):
                node_left = temp.popleft()
                node_right = temp.pop()
                if not node_left and not node_right:
                    continue
                if not node_left or not node_right or node_left.val != node_right.val:
                    return False
        
        return True
                


# 递归
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def recur(L, R):
            if not L and not R: return True
            if not L or not R or L.val != R.val: return False
            return recur(L.left, R.right) and recur(L.right, R.left)

        if not root:
            return True
        
        return recur(root.left, root.right)
        

        