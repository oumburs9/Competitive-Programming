# def groupAnagrams(strs):
#     m = {}
#     sets = set()

    
#     for s in strs:
#         sums = 0
#         for i in s:
#             sums += ord(i)
#             sets.add(sums)
        
        
#         # new_dict[list_keys[i]].append(list(list_values[i])) 
#     return m



def groupAnagrams( strs):
    ans =[]
    m = {}

    for s in strs:
        hashed = "".join(sorted(s))
        if hashed not in m:
            m[hashed] = []
        m[hashed].append(s)
    for a in m.values():
        ans.append(a)
    return ans

    res = groupAnagrams(["eat","tea","tan","ate","nat","bat"])
    print(res)











strs = ["eat","tea","tan","ate","nat","bat"]
res =groupAnagrams(strs)
print(res)
