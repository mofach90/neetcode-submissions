
class linkedList:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None



class MyStack:

    def __init__(self):
        self.head = linkedList(0)
        self.tail = linkedList(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def push(self, x: int) -> None:
        curr = linkedList(x)
        curr.prev = self.tail.prev
        curr.next = self.tail
        curr.prev.next = curr
        self.tail.prev = curr 
        check = self.head
        while check:
            print(check.val, end="->")
            check = check.next 
        print ("finish push")     
        

    def pop(self) -> int:
        curr = self.tail.prev
        curr.prev.next = self.tail
        self.tail.prev = curr.prev
        check = self.head
        while check:
            print(check.val, end="->")
            check = check.next 
        print ("finish pop")
        return curr.val 

    def top(self) -> int:
        curr = self.tail.prev
        return curr.val
        

    def empty(self) -> bool:
        if self.head.next == self.tail:
            return True
        return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()