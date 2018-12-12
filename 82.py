class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        prev = ListNode(0)
        prev.next = head
        head = prev
        curr = prev.next
        fast = curr.next
        while fast:
            if fast.val == curr.val:
                while curr.val == fast.val:
                    fast = fast.next
                    if not fast:
                        prev.next = fast
                        return head.next
                prev.next = fast
            else:
                prev = prev.next
            curr = prev.next
            fast = curr.next
        return head.next
