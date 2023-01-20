class Solution:
    def isValid(self, s: str) -> bool:
        
        dic ={
            "{":"}",
            "[":"]",
            "(":")"
        }

        
        stack = []
        for i in s:
            if i in dic:
                stack.append(i)
            elif len(stack)==0 or dic[stack.pop()] != i:
                return False
        return len(stack) == 0

# class Solution:
#     def isValid(self, s: str) -> bool:
#         dic = {")": "(", "]": "[", "}": "{"}
#         stack = []

#         for c in s:
#             if c not in dic:
#                 stack.append(c)
#                 continue
#             if not stack or stack[-1] != dic[c]:
#                 return False
#             stack.pop()

#         return not stack


                
                
                
        
        
        
        