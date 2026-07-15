class Node:
    def __init__(self,url):
        self.url = url
        self.next = None
        self.prev = None



class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepageNode = Node(homepage)
        self.right = Node(0)
        self.left = Node(0)
        self.left.next = self.homepageNode
        self.right.prev = self.homepageNode
        self.homepageNode.prev = self.left
        self.homepageNode.next = self.right
        self.curr = self.homepageNode

    def visit(self, url: str) -> None:
        NN = Node(url)
        NN.prev = self.curr
        NN.next = self.right
        self.curr.next = NN
        self.right.prev = NN
        self.curr = NN
        

    def back(self, steps: int) -> str:
        while self.curr != self.homepageNode and steps:
            self.curr = self.curr.prev
            steps -= 1
        return self.curr.url

        

    def forward(self, steps: int) -> str:
        while self.curr != self.right.prev and steps:
            self.curr = self.curr.next
            steps -= 1
        return self.curr.url
        

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)