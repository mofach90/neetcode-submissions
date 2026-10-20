class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxi = 0
        p = 0
        print(len(nums))
        for i in range(len(nums)):
            if nums[i] == 1:
                p += 1
                print(p)
                maxi = max(p,maxi)
            else:
                p = 0
        print("max cons '1':",maxi)
        return maxi

