# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        curr = head
        comp = 0
        G = set(G)
        while curr:
            test = curr
            if test.val in G:
                comp += 1
                while test:
                    if test.val not in G:
                        break;
                    else:
                        test = test.next
                curr = test
            else:
                curr = curr.next
        return comp
