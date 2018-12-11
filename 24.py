# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def ListNodeFromList(self, mlist):
        head = ListNode(0)
        curr = head
        for i in mlist:
            curr.next = ListNode(i)
            curr = curr.next
        return head.next

    def printListNode(self, head):
        rstr = ""
        while head:
            rstr = rstr + str(head.val) + " -> "
            head = head.next
        rstr = rstr + "None"

        return rstr

    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        curr = ListNode(0)
        curr.next = head
        head = curr
        # fast = curr
        while curr and curr.next and curr.next.next:
            slow = curr.next
            fast = curr.next.next
            slow.next = fast.next
            curr.next = fast
            fast.next = slow
            curr = curr.next.next
        return head.next


mlist = [1,2,3,4,5,6]
head = Solution().ListNodeFromList(mlist)
# print(Solution().printListNode(head))
head=Solution().swapPairs(head)
print(Solution().printListNode(head))
