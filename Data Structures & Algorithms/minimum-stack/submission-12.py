class MinStack:
    
    def __init__(self):
        self.arr = []

    def push(self,val):
        mini = self.arr[-1][-1] if self.arr else val
        
        mini = min(mini, val)
        self.arr.append((val,mini))

    def pop(self):
        self.arr.pop()

    def top(self) -> int:
        return self.arr[-1][0]

    def getMin(self) -> int:
        return self.arr[-1][-1]




























# class MinStack:

#     def __init__(self):
#         self.stack = [] 
#         self.mini = 0

#     def push(self, val: int) -> None:
#         self.mini = self.stack[-1][1] if self.stack else val
#         self.stack.append((val,min(self.mini,val)))
#         print(self.stack)

#     def pop(self) -> None:
#         self.stack.pop()

#     def top(self) -> int:
#         return self.stack[-1][0] if self.stack else 0

#     def getMin(self) -> int:
#         return self.stack[-1][1] if self.stack else 0
        
