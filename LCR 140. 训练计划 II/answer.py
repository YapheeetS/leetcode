# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def trainingPlan(self, head, cnt):
        """
        :type head: Optional[ListNode]
        :type cnt: int
        :rtype: Optional[ListNode]
        """
        cur = head
        length = 0
        while cur:
            cur = cur.next
            length += 1
            
        num = 0
        while num < (length - cnt):
            num += 1
            head = head.next
        
        return head