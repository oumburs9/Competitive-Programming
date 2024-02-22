class Solution:
    def decodeString(self, s: str) -> str:
        def f(s, idx):
            decoStr = ""
            num = 0

            while idx < len(s):
                if s[idx].isdigit():
                    num = num * 10 + int(s[idx])

                elif s[idx] == '[':
                    decoSubstr, idx = f(s, idx + 1)
                    decoStr += decoSubstr * num
                    num = 0

                elif s[idx] == ']':
                    return decoStr, idx

                else:
                    decoStr += s[idx] # if char


                idx += 1

            return decoStr

        return f(s, 0)
   

        # stack = []
        # res = ''

        # i = len(s) - 1
        # acc = ''
        # while i >= 0:
        #     if s[i] =='[' and stack:
        #         stack.pop()
        #         res += acc * int(s[i-1])
        #         print(res)
        #         i -= 1
            
        #     else:
        #         if s[i] == ']':
        #             stack.append(s[i])
        #         print(stack)
        #         elif s[i] and s[i].isalpha():
        #             acc = ''
        #             print('befor: ',acc)
        #             while i >= 0 and s[i-1].isalpha():
        #                 acc += s[i-1]
        #                 i -= 1
        #             print('after: ', acc)
        #     i -= 1
        # return res[::-1]

        