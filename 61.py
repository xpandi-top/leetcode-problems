# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        test = head
        total = 0
        while test:
            test = test.next
            total += 1
        k = k % total
        step = 0
        curr = ListNode(0)
        curr.next = head
        head = curr

        while step < k:
            prev = head.next
            while curr.next:
                curr_prev = curr
                curr = curr.next
            curr_prev.next = None
            curr.next = prev
            head.next = curr
            step += 1
        return head.next


