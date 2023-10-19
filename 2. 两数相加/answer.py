# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = ListNode(-1)
        pointer = res
        flag = False
        while l1 and l2:

            if flag:
                val = 1
            else:
                val = 0

            if val + l1.val + l2.val >= 10:
                flag = True
                val = (val + l1.val + l2.val) % 10
            else:
                flag = False
                val = val + l1.val + l2.val
            
            node = ListNode(val)
            pointer.next = node
            pointer = pointer.next
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            if flag:
                val = 1
            else:
                val = 0
            
            if val + l1.val  >= 10:
                flag = True
                val = (val + l1.val) % 10
            else:
                flag = False
                val = val + l1.val
            
            node = ListNode(val)
            pointer.next = node
            pointer = pointer.next
            l1 = l1.next
        
        while l2:
            if flag:
                val = 1
            else:
                val = 0
            
            if val + l2.val  >= 10:
                flag = True
                val = (val + l2.val) % 10
            else:
                flag = False
                val = val + l2.val
            
            node = ListNode(val)
            pointer.next = node
            pointer = pointer.next
            l2 = l2.next
        
        if flag:
            node = ListNode(1)
            pointer.next = node
        
        return res.next
            

            

# 优化代码
# 1. flag可以用数字表示，不用判断直接加
# 2.  while l1 and l2 可以改成  while l1 or l2，在循环里判断l1和l2是否为None
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
        res = ListNode() # 固定头部
        pointer = res # 可移动的指针
        carry = 0 # 进位
        while l1 or l2 or carry:
            carry = carry + (l1.val if l1 else 0) + (l2.val if l2 else 0)
            pointer.next = ListNode(carry % 10)
            carry = carry // 10
            pointer = pointer.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        return res.next

            
            

            

        