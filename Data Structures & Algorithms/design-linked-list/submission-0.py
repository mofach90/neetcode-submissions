

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class MyLinkedList:

    def __init__(self):
        self.right = Node(0)
        self.left = Node(0)
        self.left.next = self.right
        self.right.prev = self.left
        

    def get(self, index: int) -> int:
        curr = self.left.next
        while curr and index:
            curr = curr.next
            index -= 1
        if not curr or curr == self.right:
            return -1
        else:
            return curr.val
        

    def addAtHead(self, val: int) -> None:
        curr = self.left.next
        NN = Node(val)
        self.left.next = NN
        NN.prev = self.left
        NN.next = curr
        curr.prev = NN
        

    def addAtTail(self, val: int) -> None:
        curr = self.right.prev
        NN = Node(val)
        self.right.prev = NN
        NN.next = self.right
        NN.prev = curr
        curr.next = NN

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.left.next
        NN = Node(val)
        while curr and index:
            curr = curr.next
            index -= 1
        if index:
            return None
        NN.prev = curr.prev
        NN.prev.next = NN
        NN.next = curr
        curr.prev = NN

    def deleteAtIndex(self, index: int) -> None:
        curr = self.left.next
        while curr and index:
            curr = curr.next
            index -= 1
        if index or curr == self.right:
            return
        curr.next.prev = curr.prev
        curr.prev.next = curr.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)