class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n:
            return head
        prev = ListNode(0)
        prev.next = head
        head = prev
        curr = head.next
        end = None
        temp = None
        for i in range(m - 1):
            prev = curr
            curr = curr.next
        for i in range(n - m + 1):
            fast = curr.next
            curr.next = end
            if i == 0:
                temp = curr
            end = curr
            curr = fast
        prev.next = end
        temp.next = fast
        return head.next
