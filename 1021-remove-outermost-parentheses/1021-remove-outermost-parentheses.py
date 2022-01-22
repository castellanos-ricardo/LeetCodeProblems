class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = ''
        j=0
        stack = []
        for p in s:
            if j ==1 and p == ')':
                j -= 1
                stack.pop()
                continue
            if j>0 and stack:
                result += p
            if p == '(':
                stack.append(p)
                j += 1
            else:
                stack.pop()
                j -= 1
        return result
