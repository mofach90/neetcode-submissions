
class Node:
    def __init__(self,val):
        self.val = val
        self.next = None


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.lenth = 0

    def addAtHead(self, val: int) -> None:
        NN = Node(val)
        if self.lenth:
            NN.next = self.head
            self.head = NN
        else:
            self.head = self.tail = NN
        self.lenth += 1
    def addAtTail(self, val: int) -> None:
        NN = Node(val)
        if self.lenth:
            self.tail.next = NN
            self.tail = NN
        else:
            self.tail = self.head = NN
        self.lenth += 1
    def get(self, index: int) -> int:
        if not (0 <= index < self.lenth):
            return -1
        count = 0
        curr = self.head
        while count < index:
            curr = curr.next
            count += 1
        return curr.val
    
    def addAtIndex(self, index :int, val :int) -> None:
        if not (0 <= index <= self.lenth):
            return
        if index == 0:
            self.addAtHead(val)
        elif index == self.lenth:
            self.addAtTail(val)
        else:
            NN = Node(val)
            curr = self.head
            count = 0
            while count < (index - 1):
                curr = curr.next
                count += 1
            NN.next = curr.next
            curr.next = NN
            self.lenth += 1
    def deleteAtIndex(self, index: int) -> None:
        if not (0 <= index < self.lenth):
            return -1
        if self.lenth < 2:
            self.tail = self.head = None
            self.lenth = 0
            return
        if index == 0:
            self.head = self.head.next
            self.lenth -= 1
            return
        curr = self.head
        if index == (self.lenth - 1):
            while curr.next.next:
                curr = curr.next
            curr.next = None
            self.tail = curr
            self.lenth -= 1
            return
        count = 0
        while count < (index-1):
            count += 1
            curr = curr.next
        curr.next = curr.next.next
        self.lenth -= 1

test = MyLinkedList()
test.addAtHead(5)
test.addAtTail(2)
test.addAtTail(3)
test.addAtTail(6)
test.addAtTail(1)
test.addAtHead(9)
check = test.head
while check:
    print(check.val, end=" -> ")
    check = check.next
print("get= ",test.get(5))
test.addAtIndex(1,0)
check = test.head
while check:
    print(check.val, end=" -> ")
    check = check.next


        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(5)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)