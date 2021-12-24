class Solution:
    def isValid(self, s: str) -> bool:
        cp = {')':'(','}':'{',']':'['}
        stack = []
        
        for l in s:
            if l in cp:
                if stack and stack[-1] == cp[l]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(l)
        return False if stack else True
        