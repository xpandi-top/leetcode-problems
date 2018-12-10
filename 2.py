# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        elif not l2:
            return l1
        head = l1
        k = 0
        while l1 or l2:
            temp = l1.val + l2.val + k
            k = temp // 10
            temp = temp % 10
            l1.val = temp
            if not l1.next and l2.next:
                l1.next = ListNode(0)
            elif not l2.next and l1.next:
                l2.next = ListNode(0)
            elif not l1.next and not l2.next and k > 0:
                l1.next = ListNode(0)
                l2.next = ListNode(0)
            l1 = l1.next
            l2 = l2.next
        return head
