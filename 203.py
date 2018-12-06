# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        prev = None
        curr = head
        while curr :
            if curr.val == val:
                if not prev:
                    head = curr.next
                else:
                    prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return head
            

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
head = s.LinkedListfromList([1])
string = s.LinkedList2Str(s.removeElements(head, 2))
print(string)
