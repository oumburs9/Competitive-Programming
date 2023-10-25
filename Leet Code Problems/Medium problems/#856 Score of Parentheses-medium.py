class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        st = []
        score = 0
        for ch in s:
            if ch == '(':
                st.append(score)
                score = 0
            else:
                score = st.pop() + max(2 * score, 1)
        return score