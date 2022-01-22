class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = ''
        j=0
        for p in s:
            if j ==1 and p == ')':
                j -= 1
                continue
            if j>0:
                result += p
            if p == '(':
                j += 1
            else:
                j -= 1
        return result
