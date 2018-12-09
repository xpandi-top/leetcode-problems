class MyLinkedNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.length = 0

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        # content, length = self.printLinkedList()
        # print(content, length)
        if self.length <= index or index < 0:
            return -1
        head = self.head
        if not head:
            return -1
        for i in range(index):
            head = head.next
        return head.val

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        head = self.head
        prev = MyLinkedNode(val)
        prev.next = head
        self.head = prev
        self.length += 1

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        head = self.head
        if not head:
            head = MyLinkedNode(val)
            self.head = head
        else:
            while head.next:
                head = head.next
            head.next = MyLinkedNode(val)
        self.length += 1

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        head = self.head
        if index == self.length:
            self.addAtTail(val)
        elif index == 0:
            self.addAtHead(val)
        elif 0 < index < self.length:
            head = self.head
            for i in range(index):
                prev = head
                head = head.next
            addList = MyLinkedNode(val)
            addList.next = head
            prev.next = addList
            self.length += 1

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        head = self.head
        if index == 0:
            self.head = head.next
        elif 0 < index < self.length:
            dele = head
            for i in range(index):
                prev = dele
                dele = dele.next
                fast = dele.next
            prev.next = fast
        if 0 <= index < self.length:
            self.length -= 1

#     def printLinkedList(self):
#         head = self.head
#         l = []
#         while head:
#             l.append(head.val)
#             head = head.next
#         return l,self.length


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)