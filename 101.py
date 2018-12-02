
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isEqual(self,nleft,nright):
        if nleft==None or nright==None:
            if nleft==nright:
                return True
        elif nleft.val==nright.val:
            if self.isEqual(nleft.left,nright.right):
                if self.isEqual(nleft.right,nright.left):
                    return True
        return False


    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        nleft=root.left
        nright=root.right
        if nleft == None or nright==None:
            if nleft==nright:
                return True
            else:
                return False
        return self.isEqual(nleft,nright)

