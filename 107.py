
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]]
        """
        mlist=[]
        if root==None:
            mlist=[]
            temp = [root]
            ntemp = []
            child = []
            while temp!=[]:
                for i in temp:
                    if i!=None:
                        child.append(i.val)
                        ntemp.append(i.left)
                        ntemp.append(i.right)
                mlist.append([child])
                temp=[x for x in ntemp]
                ntemp=[]
        return mlist