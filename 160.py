# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        a = 0
        b = 0
        newA = headA
        newB = headB
        while headA:
            headA = headA.next
            a += 1
        while headB:
            headB = headB.next
            b += 1
        if a < b:
            k = a
            a = b
            b = k
            temp = newA
            newA = newB
            newB = temp
        for i in range(a - b):
            newA = newA.next
        while newA != newB and newA and newB:
            newA = newA.next
            newB = newB.next
        print(self.LinkedList2Str(newA))
        return newA

    def LinkedList2Str(self, head):
        contents = []
        while head:
            contents.append(head.val)
            head = head.next
        return " -> ".join([str(i) for i in contents])

    def LinkedListfromList(self, l):
        head = ListNode(l[0])
        tmp = head
        for i in range(1, len(l)):
            tmp.next = ListNode(l[i])
            tmp = tmp.next
        return head


headA = [1]
headB = [1]
headA = Solution().LinkedListfromList(headA)
headB = Solution().LinkedListfromList(headB)
results = Solution().getIntersectionNode(headA, headB)
Solution().LinkedList2Str(results)
