# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        predecessor = p = None
        temp = None
        currentNode = c = head
        while c:
            temp = c.next
            c.next = p 
            p = c
            c = temp
        return p











# “What exactly is the input structure?”
# a head pointer of a sigle linked list with 
#  “What does the requested transformation mean inside that structure?”
# first i need to thnk about what does it mean reversed list
# that means the tail of the sda will become the head
# each node,next will now point on his ancesstor rathen then successor
#  “What condition would show that the transformation is complete?”
#  old tail = new head  or old head become new tail and each new node.next == each previous node


















# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         # last case when the recurssion should abort
#         if head is None:
#             return None
#         # What shoud happens before this avoidable case:
#         # I have head = last node
#         # This last node is my new Head , means:
#         newHead = head
        
#         # if that a recurssion what shoudl i do i the case before the last case
#         # i need to link the next node to this current node
#         # head.next.next= head 
#         # that should be done recussivly that mean before t linking the next node i need to call the same function
#         # but with the next node
#         print("before",head.next)
#         if head.next:
#             self.reverseList(head.next)
#             head.next.next = head
#             print("after",head.next.next)
#         head.next = None
#         # I need to return the this new Head inforamtrion
        


    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     current = head
    #     prev = None
    #     while current:
    #         tmp = current.next
    #         current.next = prev
    #         prev = current
    #         current = tmp
    #     return prev








# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val):
#         self.val = val
#         self.next = None

# node1 = ListNode(1)
# node2 = ListNode(5)
# node3 = ListNode(10)
# node4 = ListNode(8)
# node1.next = node2
# node2.next = node3
# node3.next = node4

# current = node1


# print("The LinkedList: ")
# while current is not None:
#     print(current.val, end=" -> ")
#     current = current.next
# print("null")

# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         print("head.next:",head.next)
#         print("head.val: ",head.val)
#         print(head)
#         current = head
#         temp = None
        
#         while current is not None:
#             print("current.next:",current.next)
#             print("current.val: ",current.val)
#             temp = current
#             current = temp.next
#         def test (current):
#             if current.next != None:
#                 current = current.next
#                 test(current)
            

#         return head

