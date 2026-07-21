class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        pl  = 0
        l = len(nums)
        pr = l - 1
        if l == 1:
            return 0 if nums[0] == val else 0
        
        while pl <= pr:
            print("pl, pr", pl, pr)
            if nums[pl] == val and nums[pr] == val:
                pr -= 1
                
            elif nums[pl] == val and nums[pr] != val:
                nums[pl], nums[pr] = nums[pr], nums[pl]
                pl += 1
            else:
                pl +=1
            print(" after pl, pr", pl, pr)
            print(nums)

        return pl

                





# # brute force
# class Solution:
#     def removeElement(self, nums: list[int], val: int) -> int:
#         l = len(nums)

#         for n in range(l):
#             for i in range(l-1):
#                 if nums[i] == val:
#                     nums[i],nums[i+1] = nums[i+1], nums[i]
#         for num in nums:
#             if num == val:
#                 l -= 1
#         return l




# class Solution:
#     def removeElement(self, nums: list[int], val: int) -> int:
#         k = 0
#         for i in range(len(nums)):
#             if nums[i] != val:
#                 print("k = ",k)
#                 print(f"num {i} before =",nums)
#                 nums[k] = nums[i]
#                 print(f"num {i} after =",nums)
#                 k += 1
#         return k
# class Solution:
#     def removeElement(self, nums: list[int], val: int) -> int:
#         pointer1=-1
#         m = 0
#         k=0
#         for i in range(len(nums)):
#             if nums[i] == val:
#                 if pointer1 == -1:
#                     pointer1 =i
#                 for j in range( pointer1, len(nums)):
#                     if nums[j] != val:
#                         pointer1 = j+1
#                         nums[i],nums[j]=nums[j],nums[i]
#                         m +=1
#                         break
#                     if pointer1 == len(nums):
#                         break
#             if nums[i] != val:
#                 k += 1
#         return k



# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         i = 0
#         j=0
#         k=0
#         pointer1 = 0
#         l = len(nums)
#         for i in range(len(nums)):
#             while nums[i] == val:
#                 pointer1 += 1
#                 # print("pointer1=",pointer1) 
#                 # print(f"num {i} before =",nums) 
#                 nums[i] = "_"
#                 # print(f"num {i} after =",nums) 
#                 nums[i],nums[l-pointer1] = nums[l-pointer1],nums[i]
#                 # print(f"num {i} final =",nums) 
                
#         k = len(nums) - pointer1
#         # print("k=",k)
#         return k

# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         i = 0
#         j=0
#         k=0
#         pointer1 = 0
#         for i in range(len(nums)):
#             while nums[i] == val:
#                 pointer1 += 1
#                 print("pointer1=",pointer1) 
#                 print(f"num {i} before =",nums) 
#                 nums[i] = "_"
#                 print(f"num {i} after =",nums) 
#                 for j in range(i, (len(nums)-1)):
#                     nums[j],nums[j+1] = nums[j+1],nums[j]
#                 print(f"num {i} final =",nums) 
                
#         k = len(nums) - pointer1
#         print("k=",k)
#         return k




            





# nums --> array of int
# val intege
# remove all val from nums = Override with "_"
# return how much numbers are not equal to val in muns --> k