class Solution:
    def middleNode_v1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node = head
        flag = 1
        i = -1
        while flag == 1:
           tempnode = node
           if i >0:
              for j in range(i):
                 tempnode = tempnode.next
           if tempnode.next==None or tempnode.next.next==None:
              flag = 0
              head = node
              if i<0 and tempnode.next!=None:
                    head=node.next
           else:
              node = node.next
              i=i+1
        return head
        
    def middleNode(self, head):
        slow = head
        fast = head
        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
        return slow

