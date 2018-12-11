# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev

    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head:
            return head
        curr = head
        curr_fast = head
        slow = curr
        fast = curr
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        if not fast:
            middle = prev
        elif not fast.next:
            middle = slow
        comp = self.reverseList(middle.next)
        middle.next = None
        while comp:
            curr_fast = curr_fast.next
            curr.next = comp
            comp = comp.next
            curr.next.next = curr_fast
            curr = curr_fast
