class MyStack:

    def __init__(self):
        self.q = deque()
        

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        i = 0
        for i in range(len(self.q)-1):
            b = 0
            print ("old queue")
            for b in range(len(self.q)-1):
                print(self.q[b])
            
            print ("start")
            print(self.q[i])
            curr = self.q.popleft()
            print("curr", curr)
            self.push(curr)
            b = 0
            print ("new queue")
            for b in range(len(self.q)):
                print(self.q[b])
        return self.q.popleft()

        

    def top(self) -> int:
        return self.q[-1]
        

    def empty(self) -> bool:
        if self.q:
            return False
        return True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()