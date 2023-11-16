# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        a_list = []
        p_a = headA
        while p_a:
            a_list.append(p_a.val)
            p_a = p_a.next
        p_b = headB
        while p_b:
            if p_b.val in a_list:
                return p_b
            else:
                p_b = p_b.next
        
        return None
        


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        A, B = headA, headB
        while A != B:
            A = A.next if A else headB
            B = B.next if B else headA
        return A

