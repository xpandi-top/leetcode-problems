# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        prev = ListNode(0)
        prev.next = head
        left = head
        head = prev
        right = ListNode(0)
        righthead = right
        while left:
            # print(left.val)
            if left.val >= x:
                right.next = left
                right = right.next
                left = left.next
                prev.next = left
            else:
                prev = left
                left = left.next
        right.next = None
        prev.next = righthead.next
        return head.next
