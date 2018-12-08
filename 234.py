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
    def reverseLinkedList(self, head):
        curr = head
        prev = None
        fast = None
        while curr:
            fast = curr.next
            curr.next = prev
            prev = curr
            curr = fast
        return prev

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        curr = head
        comp = head
        i = 0
        while curr:
            curr = curr.next
            i += 1

        for j in range(i // 2):
            comp = comp.next

        comp = self.reverseLinkedList(comp)

        while comp:
            if comp.val == head.val:
                comp = comp.next
                head = head.next
            else:
                return False
        return True

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

    def hani_reverse_list(self, head):
        prev = None
        fast = None
        while head:
            fast = head.next
            head.next = prev
            prev = head
            head = fast
        return prev


s = Solution()
head = s.LinkedListfromList([1, 2, 3, 4, 5, 6])
print(s.LinkedList2Str(head))
print(s.LinkedList2Str(s.hani_reverse_list(head)))
