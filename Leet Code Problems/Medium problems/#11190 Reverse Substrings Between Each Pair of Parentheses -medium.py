class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] != ')':
                stack.append(s[i])
            else:
                st = []
                while len(stack)!=0 and stack[-1]!='(':
                    st.append(stack.pop())
                stack.pop()
                st = st[::-1]
                while len(st)!=0:
                    stack.append(st.pop())
        return "".join(stack)