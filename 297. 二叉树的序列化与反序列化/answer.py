# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return '[]'
        res = []
        deque = collections.deque()
        deque.append(root)
        while deque:
            node = deque.popleft()
            if node:
                deque.append(node.left)
                deque.append(node.right)
                res.append(str(node.val))
            else:
                res.append('null')
        return '[' + ','.join(res) + ']'


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == '[]': return None
        data = data[1:-1].split(',')
        root = TreeNode(int(data[0]))
        deque = collections.deque()
        deque.append(root)
        i = 1
        while deque:
            node = deque.popleft()
            if data[i] != 'null':
                node.left = TreeNode(int(data[i]))
                deque.append(node.left)
            i += 1
            if data[i] != 'null':
                node.right = TreeNode(int(data[i]))
                deque.append(node.right)
            i += 1
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))