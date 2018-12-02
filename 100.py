# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p==None or q == None:
            if p ==None and q==None:
                return True
            else:
                return False
        if p.val == q.val:
            if self.isSameTree(p.left, q.left):
                if self.isSameTree(p.right, q.right):
                    return True
        return False

