# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def printList(self, head):
        s = ""
        while head:
            s = s + "->" + str(head.val)
            head = head.next
        print(s)

    def addListValue(self, h1, h2):
        k = 0
        if not h1.next:
            temp = h1.val + h2.val
            k = temp // 10
            h1.val = temp % 10
        else:
            k = self.addListValue(h1.next, h2.next)
            temp = h1.val + h2.val + k
            h1.val = temp % 10
            k = temp // 10
        return k

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        h1 = l1
        h2 = l2
        a = 0
        b = 0
        while h1:
            a += 1
            h1 = h1.next
        while h2:
            b += 1
            h2 = h2.next
        if a < b:
            temp = a
            a = b
            b = temp
            temp = l1
            l1 = l2
            l2 = temp
        if a - b > 0:
            h2 = ListNode(0)
            addl = h2
            for i in range(a - b):
                h2.next = ListNode(0)
                h2 = h2.next
            h2.next = l2
            addl = addl.next
        else:
            addl = l2
        k = self.addListValue(l1, addl)
        if k == 1:
            head = ListNode(1)
            head.next = l1
        else:
            head = l1
        return head
