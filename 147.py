class Solution(object):
    def insert(self, head, drop, tail):
        if drop.val < head.val:
            drop.next = head
            head = drop
        elif drop.val >= tail.val:
            tail.next = drop
            tail = drop
        else:
            curr = head.next
            prev = head
            while curr and curr != tail.next:
                if curr.val > drop.val:
                    prev.next = drop
                    drop.next = curr
                    break
                prev = curr
                curr = curr.next
        drop = tail.next
        return head, tail, drop

    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        curr = head
        tail = head
        drop = tail.next
        while drop:
            tail.next = drop.next
            head, tail, drop = self.insert(head, drop, tail)
        return head
