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
            temp = collections.deque()
            for _ in range(len(deque)):
                node = deque.popleft()
                if node:
                    res.append(str(node.val))
                    temp.append(node.left)
                    temp.append(node.right)
                else:
                    res.append('null')
            deque = temp
        return '[' + ','.join(res) + ']'

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data=="[]": return
        vals = data[1:-1].split(',')
        root = TreeNode(int(vals[0]))
        i = 1
        queue = collections.deque()
        queue.append(root)
        while(queue):
            node = queue.popleft()
            if vals[i] != 'null':
                node.left = TreeNode(vals[i])
                queue.append(node.left)
            i += 1
            if vals[i] != 'null':
                node.right = TreeNode(vals[i])
                queue.append(node.right)
            i += 1
        return root


        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))