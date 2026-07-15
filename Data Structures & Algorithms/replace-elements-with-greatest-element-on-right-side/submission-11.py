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
class Solution:
    def new_arr(self,j,k,arr):
        # print("j=",j)
        if j < k:
            arr[j] = max(arr[j+1], self.new_arr(j+1,k,arr))
        else:
            arr[j] = -1
        return arr [j]
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr)-1:
            arr[0] = max(arr[1], self.new_arr(1,len(arr)-1,arr))
        arr[len(arr)-1] = -1
        return arr









# arr is array
# arr[i] = the greatest element in range(arr[i],len(arr))
# last element override with -1