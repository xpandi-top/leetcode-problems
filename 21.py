# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None:
            return l2
        elif l2 == None:
            return l1

        head = ListNode(0)
        newl = head 
        while l1 != None or l2 != None:
            print(l2.next)
            if l1 == None:
                newl.next = l2
                l2 = None
            elif l2 == None:
                newl.next = l1
                l1 = None
            elif l1.val>l2.val:
                newl.next = l2
                newl=newl.next
                l2 = l2.next
            elif l1.val<=l2.val:
                newl.next = l1
                newl = newl.next
                l1 = l1.next
        
        return head.next
    
    def ConvertListNode(self, l):
        if l == None:
            return 0
        printList = []
        while l != None:
            printList.append(l.val)
            l = l.next
        return printList

    def CreateListNode(self, l):
        # l is list
        head = ListNode(0)
        newl = head
        for i in l:
            newl.next=ListNode(i)
            newl = newl.next
        return head.next

a = []
b = []
print(a,"\n",b)
l1 =Solution().CreateListNode(a)
l2 =Solution().CreateListNode(b)
#print(Solution().ConvertListNode(l))
newl = Solution().mergeTwoLists(l1,l2)
print(Solution().ConvertListNode(newl))

