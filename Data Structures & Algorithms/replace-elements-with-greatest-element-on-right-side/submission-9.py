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
            return arr[j]
        return -1
    def replaceElements(self, arr: List[int]) -> List[int]:
        i = 0
        j=0
        k= len(arr)-1
        if k:
            arr[i] = max(arr[i+1], self.new_arr(i+1,k,arr))
        arr[len(arr)-1] = -1
        return arr









# arr is array
# arr[i] = the greatest element in range(arr[i],len(arr))
# last element override with -1