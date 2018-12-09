# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        curr = head
        prev = head
        keep = head
        for i in range(n):
            curr = curr.next
        while curr:
            keep = prev
            prev = prev.next
            curr = curr.next
        if prev == head:
            head = head.next
        else:
            keep.next = prev.next
        return head

