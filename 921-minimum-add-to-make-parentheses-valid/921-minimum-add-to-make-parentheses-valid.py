class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        res = 0
        for p in s:
            if p == '(':
                stack.append(p)
            elif p == ')' and stack:
                stack.pop()
            elif p == ')':
                res += 1
        
        return  res + len(stack)

        