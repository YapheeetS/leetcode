# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def trainningPlan(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        pointer = None
        while head:
            temp = head.next
            head.next = pointer
            pointer = head
            head = temp
        return pointer