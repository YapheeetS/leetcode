# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBookList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        # res = head
        pointer = None
        while head:
            temp = head.next
            head.next = pointer
            pointer = head
            head = temp
        
        book_list = []
        while pointer:
            book_list.append(pointer.val) 
            pointer = pointer.next

        return book_list