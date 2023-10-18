# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        result = ListNode()
        pointer = result

        while (list1 and list2):
            print(result)
            if list1.val <= list2.val:
                pointer.next = list1
                list1 = list1.next
                pointer = pointer.next
            else:
                pointer.next = list2
                list2 = list2.next
                pointer = pointer.next
        
        if list1:
            pointer.next = list1
        else:
            pointer.next = list2
        
        return result.next





