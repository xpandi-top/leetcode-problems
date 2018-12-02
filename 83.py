# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        newl = head
        if newl==None:
            return head
        while newl.next != None:
            if newl.next.val == newl.val:
                newl.next = newl.next.next
            else:
                newl = newl.next
        return head