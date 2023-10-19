# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1 = self.reverseList(l1)
        l2 = self.reverseList(l2)
        return self.reverseList(self.addNumber(l1, l2))
    

    def reverseList(self, l):
        curr = l
        prev = None
        while(curr):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev
    
    def addNumber(self, l1, l2):
        res = ListNode()
        pointer = res
        carry = 0
        while l1 or l2 or carry:
            carry = carry + (l1.val if l1 else 0) + (l2.val if l2 else 0)
            node = ListNode(carry % 10)
            pointer.next = node
            carry = carry // 10
            pointer = pointer.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        return res.next



        