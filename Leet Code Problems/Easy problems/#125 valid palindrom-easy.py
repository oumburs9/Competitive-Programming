class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not self.alphanum(s[l]):
                l += 1
            while l < r and not self.alphanum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

    def alphanum(self, c):
        return (
            ord("A") <= ord(c) <= ord("Z")
            or ord("a") <= ord(c) <= ord("z")
            or ord("0") <= ord(c) <= ord("9")
        )


# s = s.replace(/[^A-Za-z0-9]/g, "" )
# def isPalindrome(s:str) -> bool:
#     ss =""
#     for item in s:
#         if( ord("a") <= ord(item)<= ord("z") or ord("A")<=ord(item)<= ord("Z") or ord("0")<=ord(item)<= ord("9")):
#             ss += item.lower()
#     first = 0
#     last = len(ss)-1
#     while(first <= last):
#         if ss[first]!=ss[last]:
#             return False
#         first +=1
#         last -=1
#     return True

# res = isPalindrome("race a car")
# print(res)
