"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head: return None
        cur = head
        # 复制各节点，并建立 “原节点 -> 新节点” 的 Map 映射
        dic = {}
        while cur:
            dic[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        # 构建新节点的 next 和 random 指向
        while cur:
            dic[cur].next = dic.get(cur.next)
            dic[cur].random = dic.get(cur.random)
            cur = cur.next
        return dic[head]
        