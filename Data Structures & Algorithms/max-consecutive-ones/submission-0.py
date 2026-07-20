class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxi = 0
        i = 0
        j = 0
        while i < range(len(nums)):
            if nums[i] == 1:
                j = i
                while nums[j] and j < len(nums):
                    j += 1
                maxi = max(maxi, j - i)
                i = j
            i += 1
        print(maxi)
        return maxi 




























# class Solution:
#     def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
#         max_num = 0
#         count = 0
#         for i in range(len(nums)):
#             if nums[i] != 0:
#                 count += 1
#                 max_num = max(max_num, count)
#                 print(max_num)
#             else:
#                 count = 0
#         return max_num    


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxi = 0
        len = 0
        for i in nums:
            if i == 1:
                len += 1
            else:
                len = 0
            maxi = max(maxi, len) 
        return maxi
            
        
