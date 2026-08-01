class Node:
    def __init__(self, url):
        self.url = url
        self.next = None
        self.prev = None



class BrowserHistory:

    def __init__(self, homepage: str):
        self.HomeNode = Node(homepage)
        self.curr = self.HomeNode

    def visit(self, url: str) -> None:
        # NN = new node
        NN = Node(url)
        # successor node = SN
        if self.curr.next:
            SN = self.curr.next
            # SN.prev = None. # this in not need , the garbage collector, clean any unreachble link
        self.curr.next = NN
        NN.prev = self.curr
        self.curr = NN

    def back(self, steps: int) -> str:
        while self.curr.prev and steps:
            self.curr = self.curr.prev
            steps -= 1
        return self.curr.url

    def forward(self, steps: int) -> str:
        while self.curr.next and steps:
            self.curr = self.curr.next
            steps -= 1
        return self.curr.url

# # design : 
# - browser --> init a node with node.url = homepage , currentPage pointer = point to homepage, current page position = 0
# - visit --> this create a new node with the url , detach successot node from curr node the and attach the curr node the the new node and assign NN to curr
# - back : check if steps are valid, move to step node, return the step node url
# - forward : check if steps are valid , move to steps , return the step node

# # what state would an operation need from the previous operation
# - browderhistory = no need for any previous state
# - visit = need the current page history position
# - back = needs the current page , return the url of the position after moving backward to it
# - forward = same as back just forward 
# states  = current position number , current position url
# # what state must always be valid
# current position number 

# # translating to ds : 
# this cuold be done using SLL, but double lls could make the backward traversing easier, so you
# dont know to always start from homepage...



# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)