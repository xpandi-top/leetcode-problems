# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return None
        slow = head
        fast = head
        curr = head
        flag = 0
        i = 0
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            i += 1
            if slow == fast:
                flag = 1
                break
        if flag == 1:
            while curr != slow:
                curr = curr.next
                slow = slow.next
            return curr
        else:
            return None
