class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxi = -2
        p = -1
        for i in range(len(arr)-1, -1, -1):
            print(i)
            maxi = max(maxi, p)
            p = arr[i]
            arr[i] = maxi
        return arr





# class Solution:
#     def replaceElements(self, arr: List[int]) -> List[int]:
#         l = len(arr)
#         for i in range(l):
#             maxi = 0
#             for j in range(i+1, l):
#                 maxi = max(arr[j], maxi)
#             arr[i] = maxi
#         arr[l-1] = -1
#         return arr

# class Solution:
#     def replaceElements(self, arr: List[int]) -> List[int]:
#         i = 0
#         j=0
#         for i in range(len(arr)):
#             max_num = 0
#             for j in arr[i+1:]:
#                 # print(max_num, j)
#                 max_num = max(max_num,j)
#                 # print(max_num)
#             arr[i] = max_num
#         arr[len(arr)-1] = -1
#         return arr
# class Solution:
#     def new_arr(self,j,k,arr):
#         # print("j=",j)
#         if j < k:
#             arr[j] = max(arr[j+1], self.new_arr(j+1,k,arr))
#         else:
#             arr[j] = -1
#         return arr [j]
#     def replaceElements(self, arr: List[int]) -> List[int]:
#         if len(arr)-1:
#             arr[0] = max(arr[1], self.new_arr(1,len(arr)-1,arr))
#         arr[len(arr)-1] = -1
#         return arr

# class Solution:
#     def replaceElements(self, arr: List[int]) -> List[int]:
#         maxi = -1
#         for i in range(len(arr)-1, -1, -1):
#             temp = arr[i] 
#             arr[i] = maxi
#             maxi = max(temp,maxi)
#         return arr








# arr is array
# arr[i] = the greatest element in range(arr[i],len(arr))
# last element override with -1




# input is array arr, 
# each time you scan current element, ill check the element on his right and > 
# > replace with maximum numnber
# the last element of the array should be "-1"
# Output --> arr but modified. --> In place 

## Brute force solution: 
# one loop scan the array
# another loop check the right side element an return the maximum



# class Solution:
#     def replaceElements(self, arr: List[int]) -> List[int]:
#         temp = -1
#         maxi = -2
#         for i in range(len(arr)-1, -1, -1):
#             maxi = max(temp,maxi)
#             temp = arr[i]
#             arr[i] = maxi
#         return arr






















