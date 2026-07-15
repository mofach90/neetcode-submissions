class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j=0
        k=0
        pointer1 = 0
        l = len(nums)
        for i in range(len(nums)):
            while nums[i] == val:
                pointer1 += 1
                # print("pointer1=",pointer1) 
                # print(f"num {i} before =",nums) 
                nums[i] = "_"
                # print(f"num {i} after =",nums) 
                nums[i],nums[l-pointer1] = nums[l-pointer1],nums[i]
                # print(f"num {i} final =",nums) 
                
        k = len(nums) - pointer1
        # print("k=",k)
        return k

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