# def compress(chars) -> int:
#     indexres = 0
#     for i in range(len(chars)):
#         count = 0
#         for j in range(len(chars)):
#             if chars[i]==chars[j]:
#                 count +=1
#                 print(chars[i])
        
        
#         chars[indexres]=chars[i]
#         # indexres +=1
        
        
#         if count !=1:
#             for s in str(count):
#                 chars[indexres] = s
#                 # indexres +=1
#     return indexres
# print(compress(["a","a","b","b","c","c","c"]))

from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        cur = 0
        count = 1
        for nxt in range (1, len(chars) + 1):
            if  nxt < len(chars) and chars[nxt] == chars[nxt - 1]:
                count += 1
            else:
                chars[cur] = chars[nxt - 1]
                cur += 1
                if count > 1:
                    for i in str(count):
                        chars[cur] = i
                        cur += 1
                    count = 1
        return cur