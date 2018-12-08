# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
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
        curr = head

        for j in range(i // 2):
            comp = comp.next

        second_head = comp
        for k in range(i - (i // 2)):
            curr = comp
            # print(self.LinkedList2Str(second_head))
            comp = comp.next
            print("compnext: ", comp.val)
            if k == i - i // 2 - 1:
                curr.next = None
            comp.next = curr
        print(self.LinkedList2Str(second_head))
        return comp

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
head = s.LinkedListfromList([1,2,3,4,5,6])
print(s.LinkedList2Str(head))
print(s.LinkedList2Str(s.hani_reverse_list(head)))
