# class Solution:
#     def getConcatenation(self, nums: List[int]) -> List[int]:
#         # ans = []
#         # for i in range(len.nums):
#         #     ans
#         return [*nums,*nums]
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = nums
        for i in range(len(nums)):
            ans.append(nums[i])
        return ans



# Input array of integer nums , length n
# Output new arr of length 2n
# new arr must ans[i] == nums[i] and ans[i + n] == nums[i] 
# for 0 <= i < n (0-indexed).