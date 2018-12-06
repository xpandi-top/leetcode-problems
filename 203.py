# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        prev = None
        cur = ListNode(0)
        cur.next = head
        i = 0
        while head:
            if head.val == val and head != None:
                prev = head
                head = head.next
            else:
                print("c")
                prev = head
                head = head.next
        return cur.next

    def LinkedListfromList(self, l):
        head = ListNode(l[0])
        tmp = head
        for i in range(1, len(l)):
            tmp.next = ListNode(l[i])
            tmp = tmp.next
        return head

    def LinkedList2Str(self, head):
        contents = []
        while head:
            contents.append(head.val)
            head = head.next
        return " -> ".join([str(i) for i in contents])


s = Solution()
head = s.LinkedListfromList([1, 2, 3, 4, 5])
string = s.LinkedList2Str(head)
print(string)
