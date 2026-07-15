# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None  # this is the head of the new list
        tail = None  # this is the tail of the new list
        # we should decide where the head point, list1 or list2
        # If there is no list1, there is only one list that i ill point to it and thats all
        if not list1:
            head = list2
            return head
        # same for list2
        if not list2:
            head = list1
            return head
        # Now if both are not empty, we need to point the head to the lowest value
        if list1.val <= list2.val:
            head = list1
            list1 = list1.next # list1 is aleary assigned, we can move to list1 pointer to list1.next
        else:
            head = list2
            list2 = list2.next

        # we will move only the tail now but first we need make a link with the head
        tail = head

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else: # the list2.val is bigger than the list1.val
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        # if the list1 ended link the tail to the rest of the list2
        if list1:
            tail.next = list1
        else:
            tail.next = list2
        return head






































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
