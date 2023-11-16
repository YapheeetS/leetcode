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
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        q_list = []
        q_list.append(root)
        from_left = True
        while q_list:
            temp = []
            print(from_left)
            if from_left:
                temp = q_list
            else:
                temp = q_list[::-1]
            from_left = not from_left
            
            val_list = []
            for node in temp:
                val_list.append(node.val) 
            res.append(val_list)

            temp = q_list
            q_list = []
            for node in temp:
                if node.left:
                    q_list.append(node.left)
                if node.right:
                    q_list.append(node.right)
            
        return res
                




class Solution(object):
    def decorateRecord(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        deque = collections.deque([root])
        while deque:
            tmp = collections.deque()
            for _ in range(len(deque)):
                node = deque.popleft()
                if len(res) % 2 == 0:
                    tmp.append(node.val)
                else:
                    tmp.appendleft(node.val)
                if node.left:
                    deque.append(node.left)
                if node.right:
                    deque.append(node.right)
            res.append(list(tmp))
            
        return res
                

