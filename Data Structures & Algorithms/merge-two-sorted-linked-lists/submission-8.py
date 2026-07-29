# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        if not list1 and list2:
            return list2
        if not list2 and list1:
            return list1
        if list1.val <= list2.val:
            new_head = list1
        else: 
            new_head = list2
        curr = new_head
        while list1 and list2:
            if list1.val <= list2.val:
                prev = list1
                list1 = list1.next
            else:
                prev = list2
                list2 = list2.next
            curr.next = prev
            curr = curr.next
        if list1:
            curr.next = list1
        else: 
            curr.next = list2
        return new_head
            





# what is exactly is the input ds:
# - 2 sorted linkedlists,   i get the head of each
# what the transportation make inside the infrastructure
# - it created a new linked list that have all list1 and list2 nodes sorted
# what conition should show that the transformation is complete
# - during the transportation if one of the list had no node any more, 
# means the transforamtion is done and i can just append the rest of the node 
# to the tail of the new list because they are already sorted


# + what ionforamtion i have now: 
# - in each list, the node.val <= node.next.val
# - if i arrive to the end of a list (list.tail), the rest of the merged node can be, 
# just the rest of the longuer node -- > maybe that means i need to check what node is longuer than
# the other and merge the shorter too the longuer, but i dont have this information, that would 
# add unnecessary complexity
# + what information i dont know?
# is list1.node1.val bigger that list2.node1.val and if yes is it smaller than list2.node2.val
# + what thinking should i follow that cna bring me faster to the solution: 
# - is that a problem that i need to go experimental, checking each node when traversing, 
# or defensive, checking first what could break, or maybe recusion .Is there a pattern or sign 
# that make it more clear what thinking strategie should i go for. 










# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         head = None  # this is the head of the new list
#         tail = None  # this is the tail of the new list
#         # we should decide where the head point, list1 or list2
#         # If there is no list1, there is only one list that i ill point to it and thats all
#         if not list1:
#             head = list2
#             return head
#         # same for list2
#         if not list2:
#             head = list1
#             return head
#         # Now if both are not empty, we need to point the head to the lowest value
#         if list1.val <= list2.val:
#             head = list1
#             list1 = list1.next # list1 is aleary assigned, we can move to list1 pointer to list1.next
#         else:
#             head = list2
#             list2 = list2.next
#         # we will move only the tail now but first we need make a link with the head
#         tail = head

#         while list1 and list2:
#             if list1.val <= list2.val:
#                 tail.next = list1
#                 list1 = list1.next
#             else: # the list2.val is bigger than the list1.val
#                 tail.next = list2
#                 list2 = list2.next
#             tail = tail.next
#         # if the list1 ended link the tail to the rest of the list2
#         if list1:
#             tail.next = list1
#         else:
#             tail.next = list2
#         return head


































# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         current1 = list1
#         current2 = list2
#         # print("**** this before ***")
#         # print(f"this is list 1")  
#         # while list1:
#         #     if list1.val:
#         #         print(list1.val, end=" -> ")
#         #     list1 = list1.next
#         # print(f"this is list 2")  
#         # while list2:
#         #     if list2.val:
#         #         print(list2.val, end=" -> ")
#         #     list2 = list2.next     
           
#         temp = None
#         newList = None
#         xx = newList
#         while current1 and current2:
#             if current1.val <= current2.val:
#                 print("**** working on the current1 node ****")
#                 print(f"current1.val =< current2.val: {current1.val} =< {current2.val}")
#                 tmp = current1.next
#                 print("print current1", current1.val)
#                 # list1.next = list2
#                 print("print current1 after list1.next= list2", current1.val)
#                 if newList is None:
#                     newList = current1
#                     xx = newList
#                     print("what get assigned: ", current1)
#                 else:
#                     print("what get assigned: ", current1.val)
#                     newList.next = current1 
#                     newList = newList.next
#                 current1 = tmp
#                 if current1:
#                     print("print current1 after tmp", current1.val)

#             else:
#                 print("++++ working on the current2 node ++++")
#                 print(f"current1.val {current1.val} current2.val {current2.val}")

#                 tmp = current2.next
#                 # list2.next = list1
#                 if newList is None:
#                     print("what get assigned: ", current2)
#                     newList = current2
#                     xx = newList
#                 else:
#                     print("what get assigned: ", current2.val)
#                     newList.next = current2
#                 current2 = tmp 
#                 if current2:
#                     print("print current2 after tmp", current2.val)                  
#         # print("**** this after ***")
#         print(f"this is newLinewListst")  
#         while xx:
            
#             print(xx.val, end=" -> ")
#             xx = xx.next
  

#         # print(f"this is list 1")  
#         while list1:
#             if list1.val:
#                 print(list1.val, end=" -> ")
#             list1 = list1.next
#         print(f"this is list 2")  
#         while list2:
#             if list2.val:
#                 print(list2.val, end=" -> ")
#             list2 = list2.next      
#         return 0
