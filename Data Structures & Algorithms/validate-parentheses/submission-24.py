

class Solution:
    def isValid(self, s: str) -> bool:


        stack = []
        dic = {
            "{":"}",
            "(":")",
            "[":"]"
        }

        for i in s:
            print(i)
            if i in dic:
                stack.append(i)
            elif stack:
                if dic[stack[-1]] != i:
                    return False
                stack.pop()
            else:
                return False
        if stack:
            return False
        else :
            return True
















# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack = []
#         pairHashMap = {"}":"{", ")":"(", "]":"["}
#         print("start-stack",bool(stack))
#         for i in s:
#             if i in pairHashMap and stack:
#                 if stack[-1] != pairHashMap[i]:
#                     return False
#                 else:
#                     stack.pop()
#             else:
#                 stack.append(i)
#                 print("stack",stack)    
#         print("final-stack",stack)
#         return not bool(stack)
            

            










# class Solution:
#     def isValid(self, s: str) -> bool:
#         if len(s) % 2 != 0:
#             return False
#         check = False
#         for i in range(len(s)//2):
#             for j in range(i+1,len(s)):
#                 if ord(s[i]) == (ord(s[j])-2) or ord(s[i]) == (ord(s[j])-1):
#             if ord(s[i]) == (ord(s[i+1])-2) or ord(s[i]) == (ord(s[i+1])-1):
#                 check = True
#                 i += 1
#                 continue
#             else:
#                 for j in range(len(s)//2):
#                     if ord(s[j]) == (ord(s[j+1])-2) or ord(s[j]) == (ord(s[j+1])-1):
#                         check = True
#                         i += 1
#                         continue


#         return True



# Input string s
# s[i] =  '(', ')', '{', '}', '[' and ']'.
# Every open bracket is closed by the same type of close bracket.
# --> means you close a '(' with ')' and not a '}',
# Open brackets are closed in the correct order.
# --> "([(... here the last one opened should be first closed
# Every close bracket has a corresponding open bracket of the same type.
# --> that means for me you can not have an open not closed bracket
# True if s = "(......)", "[....]", "{....}"    
# AND True if = "([()])".     !!! False = "([(]))"
# AND True if = "([])".     !!! False = "([})"


# class Solution:
#     def isValid(self, s: str) -> bool:
#         if len(s) % 2 != 0:
#             return False
#         for i in range(len(s)//2):
#             print("hi")
#             print(ord(s[i]),ord(s[-i-1]))
#             print(ord('['),ord(']'))
#             if ord(s[i]) != (ord(s[-i-1])-2) and ord(s[i]) != (ord(s[-i-1])-1):
#                 return False
#         return True