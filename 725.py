# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        l = []
        while root:
            l.append(root.val)
            root = root.next
        n = len(l) // k
        m = len(l) % k
        rl = []
        index = 0
        if n == 0:
            for i in range(k):
                if i >= m:
                    rl.append([])
                else:
                    rl.append([l[i]])
        else:
            for i in range(k):
                if i >= m:
                    rl.append(l[index + (i - m) * n: index + (i - m + 1) * n])
                else:
                    rl.append(l[i * (n + 1): (i + 1) * (n + 1)])
                    index = (i + 1) * (n + 1)
        return rl
